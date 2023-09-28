import pandas as pd

wb = pd.read_excel("F23P1-M010-Group2.xlsx", dtype=str)
bins = list(wb["binList"])
chars = list(wb["charList"])

for i in range(len(bins)):
	print(bins[i], "; ", chars[i])
    
def str_to_bin(word: str) -> int:
    wb = pd.read_excel("F23P1-M010-Group2.xlsx", dtype=str)
    bins = list(wb["binList"])
    chars = list(wb["charList"])
    
    existing_double_char_list = ["th", "er", "on", "ss", "en", "te", "de"]
    existing_double_int_list = [1111001, 1111010, 1111011, 1111100, 1111101, 1111110]
    
    newList = []
    a = 0
    count = 0
    for i in range(len(bins)):
        if word == chars[count]:
            newList.append([bins[i]])
        count = count + 1
    if len(newList) > 1:
        a = a + bins[count]
    print(newList)
            
print(str_to_bin('jb'))



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

