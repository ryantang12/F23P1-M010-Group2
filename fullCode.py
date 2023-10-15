# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 16:14:25 2023

@author: ryan_
"""

# This function will read an excel file and print out the corresponding character and it's binary conversion
# TASK #1 (Ryan)
import pandas as pd

wb = pd.read_excel("F23P1-M010-Group2.xlsx", dtype=str)
bins = list(wb["binList"]) # stores the binary numbers in a list
chars = list(wb["charList"]) # stores the characters in a list

try:
    i = chars.index("\n")
    chars[i] = "\n"
except:
    print("\n was not found")
    
try:
    i = chars.index(" '")
    chars[i] = "'"
except:
    print("' was not found")
    
try:
    i = chars.index("<space>")
    chars[i] = " "
except:
    print("<space> was not found")

for i in range(len(bins)):
	print(bins[i], "; ", chars[i])




# Ryan Tang
# This function will read in a string and return the corresponding binary value for that string
# TASK #2
def str_to_bin(word):   
    binary = 0
    newWord = ""
    
    if word[0:2] == "\n":
        binary = "1110100"
        newWord = word[2:]
        return binary, newWord
            
    if len(word) >= 2:
        for i in range(len(chars)):
            s = word[0:2]
            if s == chars[i]:
                word = word[2:]
                binary = bins[i]
                return binary, word
        
    if len(word) >= 1:
        for i in range(len(chars)):
            if chars[i] == word[0]:
                if len(word) > 1:
                    newWord = word[1:]
                else:
                    newWord = ""
                binary = bins[i]
                return binary, newWord
            
print(str_to_bin('\n'))
print(str_to_bin('one'))
print(str_to_bin('ssep'))     
print(str_to_bin(' '))
print(str_to_bin('"hello"')) 
print(str_to_bin("hello"))



# TASK #3 (Ryan)
# This function reads in a string of binary values and returns the first binary value in the string as well as the string minus the frist binary value
def getFirstBin(string: str):
    flag = string[0]
    
    if flag == "0": # this is the short binary value
        binVal = string[0:5] # short char = 5
        string = string[5:]
    else: # this is a long binary value
        binVal = string[0:7] # long char = 7
        string = string[7:]
    return binVal, string


# This function takes a binary value as input and returns the char for that binary value
def getChar(string):
    i = bins.index(string)
    return chars[i]





###THE FUNCTION READS IN A TEXT FILE AND CREATES A NEW TEXT FILE CALLED "BinOutput.txt" THAT CONTAINS THE BINARY CODES FOR THE GIVEN FILE.###
# TASK 4 By Jiayuan Zhang (MICHAEL)# (updated by Ryan)
def txt_to_bin(file_name):
#TAKE A STRING AS INPUT TO THE FUNCTION
    f = open (file_name, "r")                    #OPEN THE FILE
    s = f.read()                                #READ IN THE VALUES
    f.close()                     
               #CLOSE THE FILE

    print(s)
#FUNCTION FIND ALL THE BINARY CODES FOR THE GIVEN TEXT FILE
    binStr = ''
    
    while (s != ''):
        # print(binStr, '\n', s) 
        binVal, s = str_to_bin(s)
        binStr = binStr + binVal                  #DETERMINE THE NUMBER OF BITS NEEDED TO STORE THE TEXT FILE
        
    print(binStr)
    numBits = len(binStr)
    binStr = str(numBits) + "." + binStr        # "." is use to separate them
        
        
#WRITE THE BINARY VALUES TO A FILE NAMED "BinOutput.txt" 
    f = open ("BinOutput.txt", "w+")
    f.write(binStr)
    f.close()
    print(binStr)

print(txt_to_bin("Hill.txt"))
# print(txt_to_bin("alma_mater.txt"))

"""
    TASK #5 - BY JACOB BIANCO
    THIS FUNCTION READS IN A TEXT FILE WITH BINARY VALUES AND
    CREATES A NEW FILE THAT CONTAINS THE CHARACTERS FOR THE
    GIVEN FILE
"""


def bin_to_txt(file_name='BinOutput.txt'):
    """
    THE FOLLOWING BLOCK OF CODE OPENS THE FILE, READS INTO THE FILE
    THEN CLOSES THE FILE
    """

    f = open(file_name, 'r')
    s = f.read()
    f.close()
    print(s)

    '''
    THE FOLLOWING BLOCK OF CODE REMOVES THE DECIMAL NUMBER AND 
    PERIOD FROM THE BEGINNING OF THE STRING 
    '''
    i = s.index(".")
    s = s[i + 1:]
    print(s)

    '''
    THE FOLLOWING BLOCK OF CODE LOOPS THROUGH A SEQUENCE OF BINARY
    NUMBERS AND APPENDS THE CHARACTER VALUE CORRESPONDING TO THAT
    BINARY VALUE AND OUTPUTS A CHARACTER STRING
    '''

    charStr = ''
    while s != '':
        binval, s = getFirstBin(s)
        charStr = charStr + getChar(binval)

    '''
    THE FOLLOWING BLOCK OF CODE PRINTS THE OUTPUTTED CHARACTER STRING
    INTO A TEXT FILE
    '''
    f = open('TextOutput.txt', 'w+')
    f.write(charStr)
    f.close()
    print(charStr)
    
print(bin_to_txt('BinOutput.txt'))


def compare_files(file1_name: str, file2_name: str = "TextOutput.txt") -> bool:
    try:
        # Open the first file and read its contents
        with open(file1_name, 'r') as file1:
            content1 = file1.read()

        # Open the second file and read its contents
        with open(file2_name, 'r') as file2:
            content2 = file2.read()

        # Check if the contents of the two files are identical
        if content1 == content2:
            return True
        else:
            return False

    except FileNotFoundError:
        print("One or both files not found.")
        return False
    
print(compare_files("Hill.txt", "TextOutput.txt"))
print(compare_files("alma_mater.txt", "TextOutput.txt"))


def are_strings_identical(string1: str, string2: str) -> bool:
    # Check if the lengths of the two strings are the same
    if len(string1) != len(string2):
        return False

    # Go through the characters of both strings and compare them
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            return False

    # If the loop completes without finding any differences, the strings are identical
    return True

print(are_strings_identical("hello", "hello"))
print(are_strings_identical("hello", "no"))

