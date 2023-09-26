import pandas as pd

wb = pd.read_excel('F23P1-M010-Group2.xlsx', dtype=str)
bins = list(wb["bin_List"])
chars = list(wb["char_List"])

for i in range(len(bins)):
	print(bins[i], "; ", chars[i])


# how to open a file
f = open("TextOutput.txt")
s1 = f.read()
print(s1)
f.close()

f = open("BinOutput.txt")
s2 = f.read()
print(s2)
f.close()

same = True
i = 0
while same:
	if s1[i] == s2[i]:
		print("still same")
	else:
		same == False
	i+=1

