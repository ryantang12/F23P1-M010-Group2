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
