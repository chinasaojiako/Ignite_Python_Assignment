#Program for the multiplication tables

print('Multiplication tables: Which number do you want to start with?')
number = int(input())
n = 1
while n <= 12 :
    times = number * n
    print(str(number) + ' * ' + str(n) + ' = ' + str(times))
    #print(times)
    n = n + 1

