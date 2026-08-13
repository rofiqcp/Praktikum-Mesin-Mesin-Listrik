duty=[20 40 60 80 100];
V=12*duty/100;
rpm=[320 690 1080 1470 1810];
plot(duty,rpm,'o-'); grid on; xlabel('Duty (%)'); ylabel('Speed (rpm)');
p=polyfit(V,rpm,1); disp('Linear approximation rpm=a*V+b'); disp(p);
