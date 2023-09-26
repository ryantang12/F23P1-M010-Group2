import pandas as pd

wb = pd.read_excel('P1Dictionary,xlsx', dtype=str)
bins = list(wb["bin_List"])
chars = list(wb["char_List"])

for i in range(len(bin)):
	print(bins[i], "; ", chars[i])
