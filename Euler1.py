#Solution for Euler problem 1.

x = 0;
sum = 0;
while(x < 1000):
    if(x%3 == 0):
        sum += x;
    elif(x%5 == 0):
        sum += x;
    x += 1;

print(sum);