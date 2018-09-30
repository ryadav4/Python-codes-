#find the largest number :

largest = -1
print('Before',largest)

for i in [1,45,67,12,100] :
    if i>largest :
        largest = i
        print(largest , i)
    else :
        print(i , 'is less than',largest)
print('largest number is :', largest)
