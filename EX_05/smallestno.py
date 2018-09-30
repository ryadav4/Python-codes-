#smallest value

smallest = 1000
print('Before',smallest)

for i in [1,0,2,-2,100] :
    if i<smallest :
        smallest = i
        print(smallest , i)
    else :
        print(i , 'is greater than',smallest)
print('smallest number is :', smallest)
