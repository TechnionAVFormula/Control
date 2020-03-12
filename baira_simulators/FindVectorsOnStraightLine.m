function [a,v,x,y,Fl,Fd,Nr,Nf,T_d,k]=FindVectorsOnStraightLine(Straight_Line,beta,m,v,dt,Fl,Fd,Nr,Nf,M,c,b,L,H,Miu,Miur,Miuf,R,A,Cd,Cl,Ro_air,g,Start_ratio,Gr,Final_ratio,T1,T2,T3,T4)

p=0;
t1=0;
t2=0;
t3=0;
k=1;

T_d=zeros;          %% Total distance of the vehicle
x=zeros;            %% Distance on x axis [m]
y=zeros;            %% Distance on y axis [m]
a=zeros;

%%Find Vectors of a,v,x,Fl,Fd,Nr,Nf for straight road
while (T_d(k)<Straight_Line)
    if v(k)<17  %%First gear
        k=k+1;
        a1(k)= b*g/(-H+L/Miu)+Fl(k-1)*b/(M*(-H+L/Miu))-Fd(k-1)/M;
        a2(k)=T1/(M*R)-Fd(k-1)/M;
        a(k)=min(a1(k),a2(k));
        v(k)=v(k-1)+a(k)*dt;
        T_d(k)=T_d(k-1)+v(k)*dt+a(k)*dt*dt/2;
        x(k)=T_d(k)*cosd(beta);
        y(k)=T_d(k)*sind(beta);
        Fl(k)=0.5*Ro_air*A*Cl*v(k)*v(k);
        Fd(k)=0.5*Ro_air*A*Cd*v(k)*v(k);
        Nr(k)=M*a(k)/Miu+Fd(k)/Miu;
        Nf(k)=M*g+Fl(k)-Nr(k);
        p=p+dt;
        t1=t1+dt;
        t2=t2+dt;
        t3=t3+dt;
    else if 17<=v(k) && v(k)<22 %%Second gear
            if p==t1
                for d=0:dt:0.040    %%Press on clatch
                    k=k+1;
                    a1(k)=-Fd(k-1)/M;
                    a(k)=a1(k);
                    v(k)=v(k-1)+a(k)*dt;
                    T_d(k)=T_d(k-1)+v(k)*dt+a(k)*dt*dt/2;
                    x(k)=T_d(k)*cosd(beta);
                    y(k)=T_d(k)*sind(beta);
                    Fl(k)=0.5*Ro_air*A*Cl*v(k)*v(k);
                    Fd(k)=0.5*Ro_air*A*Cd*v(k)*v(k);
                    Nf(k)=(M*g+Fl(k))*c/L;
                    Nr(k)=(M*g+Fl(k))-Nf(k);
                    t1=t1+dt;
                    t2=t2+dt;
                    t3=t3+dt;
                end
            else
                k=k+1;
                a1(k)= b*g/(-H+L/Miu)+Fl(k-1)*b/(M*(-H+L/Miu))-Fd(k-1)/M;
                a3(k)=T2/(M*R)-Fd(k-1)/M;
                a(k)=min(a1(k),a3(k));
                v(k)=v(k-1)+a(k)*dt;
                T_d(k)=T_d(k-1)+v(k)*dt+a(k)*dt*dt/2;
                x(k)=T_d(k)*cosd(beta);
                y(k)=T_d(k)*sind(beta);
                Fl(k)=0.5*Ro_air*A*Cl*v(k)*v(k);
                Fd(k)=0.5*Ro_air*A*Cd*v(k)*v(k);
                Nr(k)=M*a(k)/Miu+Fd(k)/Miu;
                Nf(k)=M*g+Fl(k)-Nr(k);
                t1=t1+dt;
                t2=t2+dt;
                t3=t3+dt;
            end
        else if 22<=v(k) && v(k)<28.611 %%Third gear
                if t1==t2
                    for d=0:dt:0.040    %%Press on clatch
                        k=k+1;
                        a1(k)=-Fd(k-1)/M;
                        a(k)=a1(k);
                        v(k)=v(k-1)+a(k)*dt;
                        T_d(k)=T_d(k-1)+v(k)*dt+a(k)*dt*dt/2;
                        x(k)=T_d(k)*cosd(beta);
                        y(k)=T_d(k)*sind(beta);
                        Fl(k)=0.5*Ro_air*A*Cl*v(k)*v(k);
                        Fd(k)=0.5*Ro_air*A*Cd*v(k)*v(k);
                        Nf(k)=(M*g+Fl(k))*c/L;
                        Nr(k)=(M*g+Fl(k))-Nf(k);
                        t1=t1+dt;
                        t3=t3+dt;
                    end
                else
                    k=k+1;
                    a1(k)= b*g/(-H+L/Miu)+Fl(k-1)*b/(M*(-H+L/Miu))-Fd(k-1)/M;
                    a4(k)=T3/(M*R)-Fd(k-1)/M;
                    a(k)=min(a1(k),a4(k));
                    v(k)=v(k-1)+a(k)*dt;
                    T_d(k)=T_d(k-1)+v(k)*dt+a(k)*dt*dt/2;
                    x(k)=T_d(k)*cosd(beta);
                    y(k)=T_d(k)*sind(beta);
                    Fl(k)=0.5*Ro_air*A*Cl*v(k)*v(k);
                    Fd(k)=0.5*Ro_air*A*Cd*v(k)*v(k);
                    Nr(k)=M*a(k)/Miu+Fd(k)/Miu;
                    Nf(k)=M*g+Fl(k)-Nr(k);
                    t1=t1+dt;
                    t3=t3+dt;
                end
            else if 28.611<v(k) %%Forth gear
                    if t1==t3
                        for d=0:dt:0.040    %%Press on clatch
                            k=k+1;
                            a1(k)=-Fd(k-1)/M;
                            a(k)=a1(k);
                            v(k)=v(k-1)+a(k)*dt;
                            T_d(k)=T_d(k-1)+v(k)*dt+a(k)*dt*dt/2;
                            x(k)=T_d(k)*cosd(beta);
                            y(k)=T_d(k)*sind(beta);
                            Fl(k)=0.5*Ro_air*A*Cl*v(k)*v(k);
                            Fd(k)=0.5*Ro_air*A*Cd*v(k)*v(k);
                            Nf(k)=(M*g+Fl(k))*c/L;
                            Nr(k)=(M*g+Fl(k))-Nf(k);
                            t1=t1+dt;
                        end
                    else
                        k=k+1;
                        a1(k)= b*g/(-H+L/Miu)+Fl(k-1)*b/(M*(-H+L/Miu))-Fd(k-1)/M;
                        a5(k)=T4/(M*R)-Fd(k-1)/M;
                        a(k)=min(a1(k),a5(k));
                        v(k)=v(k-1)+a(k)*dt;
                        T_d(k)=T_d(k-1)+v(k)*dt+a(k)*dt*dt/2;
                        x(k)=T_d(k)*cosd(beta);
                        y(k)=T_d(k)*sind(beta);
                        Fl(k)=0.5*Ro_air*A*Cl*v(k)*v(k);
                        Fd(k)=0.5*Ro_air*A*Cd*v(k)*v(k);
                        Nr(k)=M*a(k)/Miu+Fd(k)/Miu;
                        Nf(k)=M*g+Fl(k)-Nr(k);
                        t1=t1+dt;
                    end
                end
            end
        end
    end
end
end
