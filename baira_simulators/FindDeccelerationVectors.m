function [ad,v1,x1,y1,Fl1,Fd1,Nr1,Nf1,T_d1,X_d,p]=FindDeccelerationVectors(a,v,T_d,x,y,Fl,Fd,Nr,Nf,Va,Straight_Line,k,m,p,dt,beta,X_d,Vec_p,M_v,M_d,M,c,b,L,H,Miu,Miur,Miuf,R,A,Cd,Cl,Ro_air,g);

%%Engine Data

Start_ratio=76/31;
Gr=[2.5714 1.8824 1.4737 1.1818 0.958 0.807];   %% Gear ratio
Final_ratio=27/11;
T1=680;             %% First moment from engine [Nm]
T2=Gr(2)*T1/Gr(1);  %% Second moment from engine [Nm]
T3=Gr(3)*T2/Gr(2);  %% Third moment from engine [Nm]
T4=Gr(4)*T3/Gr(3);  %% Forth moment from engine [Nm]
T=[T1 T2 T3 T4];

ad=[a(1:p)];
v1=[v(1:p)];
T_d1=[T_d(1:p)];
x1=[x(1:p)];
y1=[y(1:p)];
Fl1=[Fl(1:p)];
Fd1=[Fd(1:p)];
Nr1=[Nr(1:p)];
Nf1=[Nf(1:p)];

if v(k)>Va(m)   %%Check if the driver can get into the turn
    
    for i=1:k   %%Find the x to start deccelerate
        p=i;
        
        Vec_p1(m)=p;
        
        ad=[a(1:p)];
        v1=[v(1:p)];
        T_d1=[T_d(1:p)];
        x1=[x(1:p)];
        y1=[y(1:p)];
        Fl1=[Fl(1:p)];
        Fd1=[Fd(1:p)];
        Nr1=[Nr(1:p)];
        Nf1=[Nf(1:p)];
        
        while T_d1(p)<Straight_Line
            p=p+1;
            ad(p)=(-Fd1(p-1)+Miuf*(Fd1(p-1)*H-M*g*c-Fl1(p-1)*c)/(L)+Miur*(-Fd1(p-1)*H-M*g*L-Fl1(p-1)*L+M*g*c+Fl1(p-1)*c)/(L))/(M-M*H*Miuf/L+M*H*Miur/L);
            v1(p)=v1(p-1)+ad(p)*dt;
            T_d1(p)=T_d1(p-1)+v(k)*dt+a(k)*dt*dt/2;
            x1(p)=T_d(p)*cosd(beta);
            y1(p)=T_d(p)*sind(beta);
            Fl1(p)=0.5*Ro_air*A*Cl*v1(p)*v1(p);
            Fd1(p)=0.5*Ro_air*A*Cd*v1(p)*v1(p);
            Nf1(p)=(-Fd1(p)+M*H*ad(p)+M*g*c+Fl1(p)*c)/L;
            Nr1(p)=M*g+Fl1(p)-Nf1(p);
        end
        
        if T_d1(p)>=Straight_Line   %%Check if the driver can get into the turn
            if v1(p)<=Va(m) && v1(p-10)>Va(m)
                if m==1
                    X_d(m)=sum(Vec_p1);
                else
                    X_d(m)=sum(Vec_p)+Vec_p1(m);
                end
                break
            end
        end
    end
end

    Vec_p1(m)=1;

    if T_d1(p)>=Straight_Line && v1(p)>=Va(m)
        v1(p)=Va(m);
        if m==1
            X_d(m)=sum(Vec_p1);
        else
            X_d(m)=sum(Vec_p)+Vec_p1(m);
        end
    end
    
    if Straight_Line==0 || X_d(m)==0
        X_d(m)=1;
    end
end

    