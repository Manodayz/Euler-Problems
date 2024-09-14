#A solution for Euler problem 2.

#Initializing variables
x = 1;
xHolder = 0;
prevX = 0;
sum = 0;

#Loop for sum.
while(x < 4000000):
    if(x % 2 == 0):
        sum += x;
    xHolder = x;
    x += prevX;
    prevX = xHolder;

print(sum);