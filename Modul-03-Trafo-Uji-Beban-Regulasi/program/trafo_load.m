load_pct=[0 25 50 75 100];
V2=[24.6 24.2 23.8 23.3 22.8];
I2=[0 2.5 5 7.5 10];
Pin=[14 70 132 195 255];
Pout=V2.*I2;
eta=100*Pout./Pin;
reg=100*(V2(1)-V2)./V2;
plot(load_pct,eta,'o-',load_pct,reg,'s-'); grid on;
xlabel('Load (%)'); legend('Efficiency','Regulation');
