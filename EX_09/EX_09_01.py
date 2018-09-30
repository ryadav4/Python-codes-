# Write a program to read through the mbox-short.txt and figure out who has the
#sent the greatest number of mail messages. The program looks for 'From ' lines
#and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a
#count of the number of times they appear in the file. After the dictionary is produced,
#the program reads through the dictionary using a maximum loop to find the most prolific committer.


fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
di = dict()
lst = list()
for line in fh:
    l1=line.split()
    for i in l1:
        if l1[0]!='From':
            continue

        k1=l1[5]
        print(k1[:2])
        di[k1]=di.get(k1,0)+1
        print(di,di[k1])
largest = -1
word = None
for k,v in di.items():
    print(k,v)

    if v>largest :
        largest =v
        word =k
print(word ,largest)
