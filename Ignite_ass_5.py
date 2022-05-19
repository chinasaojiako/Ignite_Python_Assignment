#Ask for name and print each letter out seperately on single line

print('I want to print out each letter of your name using while loop')

print('Enter your name please')
name = input()
k = 0
while k < len(name) :
    print(name[k])
    k = k + 1