# This function will read an excel file and print out the corresponding character and it's binary conversion
# TASK #1
import pandas as pd

wb = pd.read_excel(file, dtype=str)
bins = list(wb["binList"]) # stores the binary numbers in a list
chars = list(wb["charList"]) # stores the characters in a list

for i in range(len(bins)):
	print(bins[i], "; ", chars[i])




   
# This function will read in a string and return the corresponding binary value for that string
# TASK #2
def str_to_bin(word):
    wb = pd.read_excel("F23P1-M010-Group2.xlsx", dtype=str)
    bins = list(wb["binList"])
    chars = list(wb["charList"])
    
    
    existing_double_char_list = ["th", "er", "on", "ss", "en", "te", "de"]
    existing_double_int_list = [1111001, 1111010, 1111011, 1111100, 1111101, 1111110]
    newList = []
    
    binary = 0
    count = 0
    newWord = ""
    
    if len(newWord) > 1: # if the character being converted is more than one character run this statment
        for i in range(len(existing_double_char_list)):
            if newWord in existing_double_char_list:
                binary = existing_double_int_list[i]
    
    for i in range(len(bins)): # adds the character in a list to 
        if word == chars[i]:
            newWord = newWord + chars[i] # for if statement at the bottom
            newList.append([bins[i]]) # list to take binary from
        count = count + 1
    binary = newList[0]
    return binary
            
print(str_to_bin('a'))
print(str_to_bin('b'))
print(str_to_bin('te'))        





# TASK #3
# This function reads in a string of binary values and returns the first binary value in the string as well as the string minus the frist binary value
def getBFirstBin(string):
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
    wb = pd.read_excel("F23P1-M010-Group2.xlsx", dtype=str)
    bins = list(wb["binList"]) # stores the binary numbers in a list
    chars = list(wb["charList"]) # stores the characters in a list
    i = bins.index(string)
    return chars[i]





###THE FUNCTION READS IN A TEXT FILE AND CREATES A NEW TEXT FILE CALLED "BinOutput.txt" THAT CONTAINS THE BINARY CODES FOR THE GIVEN FILE.###
# TASK 4 By Jiayuan Zhang (MICHAEL)#
def txt_to_bin(file_name):
    s = ''
#TAKE A STRING AS INPUT TO THE FUNCTION
    f = open (file_name, "r")                    #OPEN THE FILE
    s1 = f.read()                                #READ IN THE VALUES
    f.close()                     
               #CLOSE THE FILE

    print(s1)
#FUNCTION FIND ALL THE BINARY CODES FOR THE GIVEN TEXT FILE
    binStr = ''
    numBits = 0
    binVal = 0
    BinStr = ''
    getBin = 0
    
    while (s != ''):
        print(binStr, '\n', s1) 
        binVals, s = getBin(s1)
        binStr = BinStr + binVal                  #DETERMINE THE NUMBER OF BITS NEEDED TO STORE THE TEXT FILE
        print(binStr)
        numBits = len(binStr)
        binStr = str(numBits) + "." + binStr        # "." is use to separate them

#WRITE THE BINARY VALUES TO A FILE NAMED "BinOutput.txt" 
    f = open ("BinOutput.txt", "w+'")
    f.write(binStr)
    f.close()
    print(binStr)





'''
    TASK #5 - BY JACOB BIANCO
    THIS FUNCTION READS IN A TEXT FILE WITH BINARY VALUES AND
    CREATES A NEW FILE THAT CONTAINS THE CHARACTERS FOR THE
    GIVEN FILE
'''

def bin_to_txt(file_name='BinOutput.txt'):
    '''
    THE FOLLOWING BLOCK OF CODE OPENS THE FILE, READS INTO THE FILE
    THEN CLOSES THE FILE
    '''

    f = open(file_name, 'r')        
    s = f.read()                    
    f.close()                    
    print(s)                        

    '''
    THE FOLLOWING BLOCK OF CODE REMOVES THE DECIMAL NUMBER AND 
    PERIOD FROM THE BEGINNING OF THE STRING 
    '''
    i = s.index(".")             
    s = [i + 1]                 
    print(s)                   

    '''
    THE FOLLOWING BLOCK OF CODE LOOPS THROUGH A SEQUENCE OF BINARY
    NUMBERS AND APPENDS THE CHARACTER VALUE CORRESPONDING TO THAT
    BINARY VALUE AND OUTPUTS A CHARACTER STRING
    '''

    initial = ''
    while s != '':                          
        bin_str, s = getBFirstBin(s)  
    initial += getChar(binVal)                  
    
    '''
    THE FOLLOWING BLOCK OF CODE PRINTS THE OUTPUTTED CHARACTER STRING
    INTO A TEXT FILE
    '''
    f = open('TextOutput.txt', 'w+')            
    f.write(initial)                            
    f.close()                                 
    print(initial)                              

