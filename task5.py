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
    s = [i + 1]
    print(s)

    '''
    THE FOLLOWING BLOCK OF CODE LOOPS THROUGH A SEQUENCE OF BINARY
    NUMBERS AND APPENDS THE CHARACTER VALUE CORRESPONDING TO THAT
    BINARY VALUE AND OUTPUTS A CHARACTER STRING
    '''

    initial = ''
    while s != '':
        binval, s = getBFirstBin(s)
    initial += getChar(binval)

    '''
    THE FOLLOWING BLOCK OF CODE PRINTS THE OUTPUTTED CHARACTER STRING
    INTO A TEXT FILE
    '''
    f = open('TextOutput.txt', 'w+')
    f.write(initial)
    f.close()
    print(initial)
