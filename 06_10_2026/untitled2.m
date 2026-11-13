data=load("5_6_sin.txt");
x = data(:, 1);    % 第一列
y = data(:, 2);    % 第二列

plot(x, y);
xlabel('x');
ylabel('y');
title('Data from 5_6_sin.txt');
grid on;