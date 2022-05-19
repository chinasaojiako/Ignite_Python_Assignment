#Ask for name and print each letter out seperately on single line
#also stating the character position
#using for loop

print('I want to print out the characters of your name using for-loop')
print('Enter your name please')
name = input()

for k in range(1, (len(name) + 1)) :
    print('Character ' + str(k) + ' : ' + name[k-1])