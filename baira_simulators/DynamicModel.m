close all
clear
tic

%%Car Data 
M_v=100;            %% Vehicle mass with no engine [kg]
M_d=75;             %% Driver mass [kg]
M=M_v+M_d;          %% Total mass with no engine (The mass of engine gets in engine data) [kg]
c=0.77;             %% Distance of rear wheel from CM [m]
b=0.77;             %% Distance of front wheel from CM [m]
L=b+c;              %% Wheel base [m]
H=0.25;             %% Height of CM [m]
Miu=1.5;            %% Coefficient of friction ACCELERATION
Miur=1.6;           %% Coefficient of friction DECCELERATION REAR
Miuf=1.5;           %% Coefficient of friction DECCELERATION FRONT
R=0.225;            %% Wheel radius [m]
A=1.25;             %% Area of Vehicle [m^2]
Cd=1.5;               %% Coeffiecient of drag force
Cl=4.01;               %% Coeffiecient of lift force

%%Environment data
Ro_air=1.225;       %% Air density [kg/m^3]
g=9.8;              %% Gravity acceleration [m/s^2]

%%Engine Data
x=1;   %[1,2]=[single piston, 4 pistons]
[M,Start_ratio,Gr,Final_ratio,T1,T2,T3,T4]=EngineData(x,M_v,M_d);

x=2;   %[1,2,3,4]=[BeitShean,Hockenaim,Skid Pad,75m straight line]
[Straight_Line,Sr,alpha,beta,Hiuvi]=Route(x);

X_d=zeros(1,length(Straight_Line));

Vec_p=0;
dt=0.001;
% time=0;
% time_ind=1;
% Mass=100;
% DDD=0;
% 
% for L=1.25:0.25:3
%     b=L/2;
%     c=L/2;
%     
%     DDD=DDD+1;
%     
% for M=210:280
%     Mass(time_ind)=M;
for m=1:length(Straight_Line) %%Find the matrix of motion
    
    v=zeros;            %% Velocity [m/s]
    Fl=zeros;
    Fd=zeros;
    Nr=zeros;
    Nf=zeros;
    
    if m>1
        v(1)=V_mat(m-1,p-1);
        Fl(1)=FL_mat(m-1,p-1);
        Fd(1)=FD_mat(m-1,p-1);
        Nr(1)=NR_mat(m-1,p-1);
        Nf(1)=NF_mat(m-1,p-1);
    end
    
    %Find Vectors of a,v,x,Fl,Fd,Nr,Nf for straight road
    [a,v,x,y,Fl,Fd,Nr,Nf,T_d,k]=FindVectorsOnStraightLine(Straight_Line(m),beta(m),m,v,dt,Fl,Fd,Nr,Nf,M,c,b,L,H,Miu,Miur,Miuf,R,A,Cd,Cl,Ro_air,g,Start_ratio,Gr,Final_ratio,T1,T2,T3,T4);
    
    %Find The allow velocity in turn
    Va(m)=sqrt(Miu*M*g*Sr(m)/(M-0.5*Ro_air*Cl*A*Miu*Sr(m)));
    
    if M-0.5*Ro_air*Cl*A*Miu*Sr(m)<=0
        Va(m)=1200;
    end
    
    p=k;
    
    %Find Vectors of a,v,x,Fl,Fd,Nr,Nf for decceleration
    [ad,v1,x1,y1,Fl1,Fd1,Nr1,Nf1,T_d1,X_d,p]=FindDeccelerationVectors1(a,v,T_d,x,y,Fl,Fd,Nr,Nf,Va,Straight_Line(m),k,m,p,dt,beta(m),Sr(m),X_d,Vec_p,M,c,b,L,H,Miu,Miur,Miuf,R,A,Cd,Cl,Ro_air,g,Start_ratio,Gr,Final_ratio,T1,T2,T3,T4);

    Vec_p(m)=p;
    
    p=p+1;
    d=p;
    
    %%Find Vectors of a,v,x,Fl,Fd,Nr,Nf for turn
    [ad,v1,x1,y1,Fl1,Fd1,Nr1,Nf1,p]=FindTurnVectors(ad,v1,x1,y1,Fl1,Fd1,Nr1,Nf1,Sr,m,p,d,dt,beta,alpha,Hiuvi,M,c,b,L,H,Miu,Miur,Miuf,R,A,Cd,Cl,Ro_air,g,Start_ratio,Gr,Final_ratio,T1,T2,T3,T4);
   
    Vec_p(m)=p-1;
    
    lengthx(m)=sum(Vec_p);
    lengthy(m)=sum(Vec_p);
    
    for l=1:p-1
        if m==1
            X_Co(1,l)=x1(l);
            Y_Co(1,l)=y1(l);
            V(1,l)=v1(l);
            Acceleration(1,l)=ad(l);
            FD(1,l)=Fd1(l);
            FL(1,l)=Fl1(l);
            NR(1,l)=Nr1(l);
            NF(1,l)=Nf1(l);
        else
            X_Co(1,length(X_Co)+1)=X_Co(lengthx(m-1))+x1(l);
            Y_Co(1,length(Y_Co)+1)=Y_Co(lengthx(m-1))+y1(l);
            V(1,length(V)+1)=v1(l);
            Acceleration(1,length(Acceleration)+1)=ad(l);
            FD(1,length(FD)+1)=Fd1(l);
            FL(1,length(FL)+1)=Fl1(l);
            NR(1,length(NR)+1)=Nr1(l);
            NF(1,length(NF)+1)=Nf1(l);
        end
    end
    
    V_mat(m,1:p-1)=v1(1:p-1);
    FL_mat(m,1:p-1)=Fl1(1:p-1);
    FD_mat(m,1:p-1)=Fd1(1:p-1);
    NR_mat(m,1:p-1)=Nr1(1:p-1);
    NF_mat(m,1:p-1)=Nf1(1:p-1);
end

% time(DDD,time_ind)=dt*length(X_Co);
% time_ind=time_ind+1;
% p=0;
% Vec_p=0;
%             X_Co=zeros(1,1);
%             Y_Co=zeros(1,1);
%             V(1,1)=zeros(1,1);
%             Acceleration(1,1)=zeros(1,1);
%             FD(1,1)=zeros(1,1);
%             FL(1,1)=zeros(1,1);
%             NR(1,1)=zeros(1,1);
%             NF(1,1)=zeros(1,1);
% end
% time_ind=1;
% DDD
% end

figure (1)
x=X_Co(1,1:length(X_Co));
y=real(Y_Co(1,1:length(X_Co)));
c=(V(1,1:length(X_Co)))*3.6;
y(end) = NaN;
p1=patch(x,y,c,'EdgeColor','interp','Marker','o','MarkerFaceColor','flat');
hold on;
h = colorbar;
set(get(h,'title'),'string','Velocity [km/hr]');
% p2=plot(x(X_d(1:length(Straight_Line))),y(X_d(1:length(Straight_Line))),'o','LineWidth',2, 'color',[1 0 0]);
ylabel('y[m]');
xlabel('x[m]');
% legend([p2],'Braking Points');
title('Velocity as a function of X and Y');
axis equal

% t=0;
% for j=1:(length(x)-1)
%     t(j+1)=t(j)+dt;
% end
% 
% figure(2)
% hold on;
% grid on;
% grid minor;
% plot(t,Acceleration,'linewidth',2);
% ylabel('a[m/s]');
% xlabel('t[s]');

% figure(3)
% patch(x,y,Acceleration,'EdgeColor','interp','Marker','o','MarkerFaceColor','flat');
% hold on;
% h = colorbar;
% set(get(h,'title'),'string','a[m/s^2]');
% axis equal
% 
% figure(4)
% grid on;
% grid minor;
% plot(t,NR,'linewidth',2);
% hold on;
% plot(t,NF,'linewidth',2);
% ylabel('Wheel Load [N]');
% xlabel('t [s]');
% legend('Rear Normal','Front Normal');
% 
% figure(5)
% grid on;
% plot(t,FD,'linewidth',2);
% hold on;
% plot(t,FL,'linewidth',2);
% legend('Drag force', 'Down force');
% ylabel('F[N]');
% xlabel('t[s]');
% 
% figure(6)
% load ('Vs.mat')
% ts=0:10*10^-3:6234*10^-2-10^-2-569*10^-2;
% plot(t,c)
% hold on;
% plot(ts,Vs(570:end))

% figure(6)
% plot(Mass,time,'linewidth',2);
% hold on;
% xlabel('Mass[kg]');
% ylabel('Lap Time[s]');
% legend('l=1.25 [m]','l=1.5 [m]','l=1.75 [m]','l=2 [m]','l=2.25 [m]','l=2.5 [m]','l=2.75 [m]','l=3 [m]','location','northwest')
% axis([210 280 4 4.6])
% toc