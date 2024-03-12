# Write a program to generate the Fibonacci sequence up to 100.

x,y = 0, 1
print(x)

while y < 100:
    print(y)
    x,y=y,x+y
