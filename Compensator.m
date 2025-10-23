clear all;
close all;
clc;

num = 6.0984;         
denom = [1 , 2.5529 , 0];
numc = [1 , 2.57];
denomc = [1 , 8.87];

 G = tf(num, denom);
C = tf(numc,denomc);
Gc = G * C;
F_Gc = feedback( Gc , 1);
step(F_Gc);



















%numl = [1 , 2.57];
%denoml = [1 , 11.42 , 23.6158 , 2.57];
%LOOP = tf(numl , denoml);
%step(LOOP);
% numd = 29.8432;
% denomd = [1 , 6.4582 , 29.8432];
% des = tf(numd , denomd);
% Create the transfer function
%rlocus(Gc);
% grid on;
% pzmap(des);
%title('Root locus map of the Transfer Function');
