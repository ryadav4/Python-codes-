#finding largest and smallest

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try :
        num = int(num)
    except :
        print('invalid input')
        continue
    if smallest==None :
        smallest = num
        largest = num
        continue
    if num<smallest :
        smallest = num
    elif num>largest:
        largest = num
print("Maximum is", largest)
print("Minimum is",smallest)
