#Take the product of these numbers

print('Take product of numbers')
k = [3, 7, 3, 9, 10, 25]
j = 0

sum  = 1
while j <= (len(k) - 1 ) :
    sum = sum * (k[j])
    j = j + 1
    print(sum)