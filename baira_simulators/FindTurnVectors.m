function  [ad,v1,x1,y1,Fl1,Fd1,Nr1,Nf1,p]=FindTurnVectors(ad,v1,x1,y1,Fl1,Fd1,Nr1,Nf1,Sr,m,p,d,dt,beta,alpha,Hiuvi,M,c,b,L,H,Miu,Miur,Miuf,R,A,Cd,Cl,Ro_air,g,Start_ratio,Gr,Final_ratio,T1,T2,T3,T4);

Ts=0;   %%steer time

%%Find Vectors of a,v,x,Fl,Fd,Nr,Nf for turn
while (Ts<abs(alpha(m)*pi*2*Sr(m)/((v1(p-1)))) && v1(p-1)>0)
    if (alpha(m)>=0)
        if Hiuvi(m)==1
            x1(p)=x1(d-1)+Sr(m)*sind(beta(m))-Sr(m)*sind(beta(m)-v1(p-1)*Ts*180/(Sr(m)*pi));
            y1(p)=y1(d-1)+sqrt(2*((Sr(m))^2)*(1-cos(v1(p-1)*Ts/(Sr(m))))-(x1(p)-x1(d-1))^2);
            v1(p)=v1(p-1);
            Fl1(p)=0.5*Ro_air*A*Cl*v1(p)*v1(p);
            Fd1(p)=0.5*Ro_air*A*Cd*v1(p)*v1(p);
            ad(p)=(Fl1(p)+M*g)*Miu/M;
            Nf1(p)=(M*g+Fl1(p))*c/L;
            Nr1(p)=(M*g+Fl1(p))-Nf1(p);
            p=p+1;
            Ts=Ts+dt;
        else
            x1(p)=x1(d-1)+Sr(m)*sind(beta(m))-Sr(m)*sind(beta(m)-v1(p-1)*Ts*180/(Sr(m)*pi));
            y1(p)=y1(d-1)-sqrt(2*((Sr(m))^2)*(1-cos(v1(p-1)*Ts/(Sr(m))))-(x1(p)-x1(d-1))^2);
            v1(p)=v1(p-1);
            Fl1(p)=0.5*Ro_air*A*Cl*v1(p)*v1(p);
            Fd1(p)=0.5*Ro_air*A*Cd*v1(p)*v1(p);
            ad(p)=(Fl1(p)+M*g)*Miu/M;
            Nf1(p)=(M*g+Fl1(p))*c/L;
            Nr1(p)=(M*g+Fl1(p))-Nf1(p);
            p=p+1;
            Ts=Ts+dt;
        end
    else
        if Hiuvi(m)==1
            x1(p)=x1(d-1)-Sr(m)*sind(beta(m))+Sr(m)*sind(+beta(m)+v1(p-1)*Ts*180/(Sr(m)*pi));
            y1(p)=y1(d-1)+sqrt(2*((Sr(m))^2)*(1-cos(v1(p-1)*Ts/(Sr(m))))-(x1(p)-x1(d-1))^2);
            v1(p)=v1(p-1);
            Fl1(p)=0.5*Ro_air*A*Cl*v1(p)*v1(p);
            Fd1(p)=0.5*Ro_air*A*Cd*v1(p)*v1(p);
            ad(p)=(Fl1(p)+M*g)*Miu/M;
            Nf1(p)=(M*g+Fl1(p))*c/L;
            Nr1(p)=(M*g+Fl1(p))-Nf1(p);
            p=p+1;
            Ts=Ts+dt;
        else
            x1(p)=x1(d-1)-Sr(m)*sind(beta(m))+Sr(m)*sind(beta(m)+v1(p-1)*Ts*180/(Sr(m)*pi));
            y1(p)=y1(d-1)-sqrt(2*((Sr(m))^2)*(1-cos(v1(p-1)*Ts/(Sr(m))))-(x1(p)-x1(d-1))^2);
            v1(p)=v1(p-1);
            Fl1(p)=0.5*Ro_air*A*Cl*v1(p)*v1(p);
            Fd1(p)=0.5*Ro_air*A*Cd*v1(p)*v1(p);
            ad(p)=(Fl1(p)+M*g)*Miu/M;
            Nf1(p)=(M*g+Fl1(p))*c/L;
            Nr1(p)=(M*g+Fl1(p))-Nf1(p);
            p=p+1;
            Ts=Ts+dt;
        end
    end
end
end