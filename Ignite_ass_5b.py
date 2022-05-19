#Ask for name and print each letter out seperately on single line
#also stating the character position
#using while loop

print('I want to print out the characters of your name using while loop')
print('Enter your name please')
name = input()
k = 1
while k < (len(name) + 1 ) :
    print('Character ' + str(k) + ' : ' + name[k-1])
    k = k + 1