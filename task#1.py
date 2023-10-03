# By: Ryan Tang
# This function will read an excel file and print out the corresponding character and it's binary conversion

import pandas as pd

def read_and_print_excel(file):
	wb = pd.read_excel(file, dtype=str)
	bins = list(wb["binList"])
	chars = list(wb["charList"])

	for i in range(len(bins)):
		print(bins[i], "; ", chars[i])

print(read_and_print("F23P1-M010-Group2.xlsx")

# This is the function String to Binary, which takes in a string that you want to look for and returns the corresponding binary number
def str_to_bin(word: str) -> int:
    wb = pd.read_excel("F23P1-M010-Group2.xlsx", dtype=str)
    bins = list(wb["binList"])
    chars = list(wb["charList"])

# This is a list for the strings that are more than one character long
    existing_double_char_list = ["th", "er", "on", "ss", "en", "te", "de"]
    existing_double_int_list = [1111001, 1111010, 1111011, 1111100, 1111101, 1111110]
    newList = []
    
    binary = 0
    count = 0
    newWord = ""
    for i in range(len(bins)):
        if word == chars[count]:
            newWord = newWord + chars[count]
            newList.append([bins[i]])
        count = count + 1
    binary = newList[0]
    
    number = 0
    if len(newWord) > 1:
        for i in existing_double_char_list:
            if newWord in existing_double_char_list:
                binary = existing_double_int_list[number]
            else:
                number = number + 1
    return binary
            
print(str_to_bin('<space>'))



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

