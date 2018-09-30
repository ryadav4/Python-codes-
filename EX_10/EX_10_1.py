
#10.2 Write a program to read through the mbox-short.txt
#and figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time and then
# splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
di = dict()
lst = list()
counts =0
for line in fh:
    if line.startswith("From "):
        l1=line.split()[5].split(':')


        di[l1[0]]=di.get(l1[0],0)+1
for k ,v in di.items():
    n = (k,v)
    lst.append(n)
    lst =sorted(lst)

for k,v in lst:
    print(k,v)
#largest = -1
#word = None
#for k,v in di.items() :
#    newtup = (k,v)
#    lst.append(newtup)
#
#    lst=sorted(lst)
##    for k,v in lst[:12]:
#        print(k,v)
