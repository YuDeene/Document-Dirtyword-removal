import re


#############################
# Expects to be called through MAIN.py.
#
# Expected input:   Inputfile, Config array, outputfile.
#  input is in utf-8
# 
#
# Output: A file without configarray in $CONFIG, called outputfile
#
# Function: Takes input and config, removes words in config, and puts all valid words in output.
#           Punctuation is kept, but trailing numbers will be removed. Adds additional whitespace and and EOL to the output.
#
# (C): Yu-Dean Wang, @ 3/18/2021.
#############################

def READIN(Inputfile, CONFIGARRAY, Outputfile):
    INPUT= open(Inputfile, 'r', encoding = "utf-8")
    OUTPUT = open(Outputfile, 'w', encoding = "utf-8")
    
   
    fileNotEnd = True
    while fileNotEnd:
        line = (INPUT.readline())
        if not line:
           fileNotEnd = False

        else:

            for word in line.split():
                word_lower = word.lower()
                writeword = True
                for z in range(0, len(CONFIGARRAY)):

                    #this ensures that upper/lower does not affect word removal.
                    if (re.fullmatch(CONFIGARRAY[z], word_lower)):
                        LastLetter = word[len(word)-1]
                        LastLetter_Ascii = ord(LastLetter)
                        writeword = False

                        #This is the function that allows the keep of punctuation.
                        if  ((LastLetter_Ascii >= 33 and LastLetter_Ascii <= 47) or
                        (LastLetter_Ascii >= 58 and LastLetter_Ascii <= 63) or
                       (LastLetter_Ascii >= 91 and LastLetter_Ascii <= 96) or
                       (LastLetter_Ascii >= 123 and LastLetter_Ascii <= 126) ):
                    
                            OUTPUT.write(LastLetter + " ")
                        break
                
                if writeword:
                    OUTPUT.write(word + " ")

            OUTPUT.write("\n")
    
    INPUT.close()
    OUTPUT.close()
######################################

