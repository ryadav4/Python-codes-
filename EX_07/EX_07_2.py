# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
avg=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count+1
    Line =line.strip()
    lh=Line.find('0')
    x=line[lh:]
    X=float(x)
    avg =avg+X
print('Average spam confidence:',avg/count)
