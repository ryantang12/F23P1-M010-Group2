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

    f = open(file_name, 'r')        # OPEN FILE
    s = f.read()                    # READ FILE
    f.close()                       # CLOSE FILE

    '''
    THE FOLLOWING BLOCK OF CODE REMOVES THE DECIMAL NUMBER AND 
    PERIOD FROM THE BEGINNING OF THE STRING 
    '''
    i = s.index(".")             # FINDS INDEX OF PERIOD
    s = [i + 1]                  # SETS "s" EQUAL TO THE BINARY STRING MINUS
                                 # BEGINNING DECIMAL NUMBER AND PERIOD

    '''
    THE FOLLOWING BLOCK OF CODE LOOPS THROUGH A SEQUENCE OF BINARY
    NUMBERS AND APPENDS THE CHARACTER VALUE CORRESPONDING TO THAT
    BINARY VALUE AND OUTPUTS A CHARACTER STRING
    '''

    initial = ''
    while s != '':                   # WHILE "s" IS NOT EQUAL TO AN EMPTY STRING
        bin_str, s = getFirstBin(s)  # OUTPUTS FIRST BINARY VALUE AND NEW STRING MINUS BINARY VALUE
    initial += getChar(i)            # APPENDS CHARACTER VALUE CONVERTED FROM BINARY TO A STRING
    '''
    THE FOLLOWING BLOCK OF CODE PRINTS THE OUTPUTTED CHARACTER STRING
    INTO A TEXT FILE
    '''
    f = open('TextOutput.txt', 'w+') # OPENS TEXT FILE
    f.write(initial)                 # WRITES STRING INTO TEXT FILE
    f.close()                        # CLOSES TEXT FILE
