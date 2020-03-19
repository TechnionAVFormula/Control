function [M,Start_ratio,Gr,Final_ratio,T1,T2,T3,T4]=EngineData(x,M_v,M_d);

if x==1 %First engine one piston
M_eng=30;           %%engine mass [kg]
M=M_v+M_d+M_eng;    %%total mass [kg]
Start_ratio=76/31;
Gr=[2.5714 1.8824 1.4737 1.1818 0.958 0.807];   %% Gear ratio
Final_ratio=27/11;
T1=680;             %% First moment from engine [Nm]
T2=Gr(2)*T1/Gr(1);  %% Second moment from engine [Nm]
T3=Gr(3)*T2/Gr(2);  %% Third moment from engine [Nm]
T4=Gr(4)*T3/Gr(3);  %% Forth moment from engine [Nm]
end

end