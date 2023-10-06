###THE FUNCTION READS IN A TEXT FILE AND CREATES A NEW TEXT FILE CALLED "BinOutput.txt" THAT CONTAINS THE BINARY CODES FOR THE GIVEN FILE.###
# TASK 4 By Jiayuan Zhang (MICHAEL)#
def txt_to_bin (file_name):
#TAKE A STRING AS INPUT TO THE FUNCTION
  f = open (file_name, "r")                    #OPEN THE FILE
  s1 = f.read()                                #READ IN THE VALUES
  f.close()                                    #CLOSE THE FILE

  print(s1)
#FUNCTION FIND ALL THE BINARY CODES FOR THE GIVEN TEXT FILE
  binStr = ''
  while (s != ''):
    print(binStr, '\n', s1) 
    binVals, s = getBin(s1)
    binStr = BinStr + binVal                  #DETERMINE THE NUMBER OF BITS NEEDED TO STORE THE TEXT FILE
  print(binStr)
  numBits = len(binStr)
  binStr = str(numBits + "." + binStr

#WRITE THE BINARY VALUES TO A FILE NAMED "BinOutput.txt" 
  f = open ("BinOutput.txt", "w+'")
  f.wrtie(binStr)
  f.close()
  print(binStr)
