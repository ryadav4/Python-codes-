text = "X-DSPAM-Confidence:0.8475";
Pos = text.find('0')
X = text[Pos:Pos+6]
x = float(X)
print(x)
