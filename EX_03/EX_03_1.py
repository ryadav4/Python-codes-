#Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
#Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours
#worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
#You should use input to read a string and float() to convert the string to a number.
#Do not worry about error checking the user input - assume the user types numbers properly.

hrs = input("Enter Hours:")
rate = input("rate per hour")
try :
    h = float(hrs)
    r = float(rate)
except :
    print('enter the numeric input')
    quit() #quits the whole line of code

if h<=40 :
    pay=h*r
else :
    x=h-40
    pay=40*r+x*1.5*r
print(pay)
