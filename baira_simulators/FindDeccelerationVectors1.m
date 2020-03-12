function [ad,v1,x1,y1,Fl1,Fd1,Nr1,Nf1,T_d1,X_d,p]=FindDeccelerationVectors1(a,v,T_d,x,y,Fl,Fd,Nr,Nf,Va,Straight_Line,k,m,p,dt,beta,Sr,X_d,Vec_p,M,c,b,L,H,Miu,Miur,Miuf,R,A,Cd,Cl,Ro_air,g,Start_ratio,Gr,Final_ratio,T1,T2,T3,T4);

ad=[a(1:p)];
v1=[v(1:p)];
T_d1=[T_d(1:p)];
x1=[x(1:p)];
y1=[y(1:p)];
Fl1=[Fl(1:p)];
Fd1=[Fd(1:p)];
Nr1=[Nr(1:p)];
Nf1=[Nf(1:p)];

if Sr~=0
if v(k)>Va(m)   %%Check if the driver can get into the turn
    
    E1=1;
    E3=k;
    E2=1;
    if p~=1
        if mod(p,2)==0
            E2=p/2;
          else
            E2=(p-1)/2;
        end
    end
        
    while (E2<k && E2~=0)
        
        p=E2;
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
        
        
        if v1(p)<=Va(m) && v1(p-10)>Va(m)
            if m==1
                X_d(m)=sum(Vec_p1);
            else
                X_d(m)=sum(Vec_p)+Vec_p1(m);
            end
            break
        end
        
        if v1(p)<=Va(m)
            if mod(E3-E2,2)==0
                E1=E2;
                E2=E2+(E3-E2)/2;
            else
                E1=E2;
                E2=E2+(E3-E2+1)/2;
            end
        else
            if mod(E2-E1,2)==0
                E3=E2;
                E2=E1+(E2-E1)/2;
            else
                E3=E2;
                E2=E1+(E2-E1+1)/2;
            end
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

