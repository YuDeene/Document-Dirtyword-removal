import sys, getopt

from INPUT_PROCESSOR import *
from CONFIG_PROCESSOR import *
from INPUT_CHECKER import *

#############################
# Expected input:   MAIN.py $INPUT $CONFIG 
#                   MAIN.py $INPUT $CONFIG $OUTPUT
#  $INPUT and $CONFIG are in UTF-8.
#
#
# Output: A file without words in $CONFIG, called Output.txt, or $OUTPUT
#
# Function: Takes input and config, removes words in config, and puts all valid words in output.
#           Punctuation is kept, but trailing numbers will be removed. Adds additional whitespace and and EOL to the output.
#
# (C): Yu-Dean Wang, @ 3/18/2021.
#############################
def main(argv):

    
    if not (len(sys.argv) >= 3 and len(sys.argv) <= 4):
        print ("Invalid Format. Expected Format: \\ MAIN.py $INPUT $CONFIG \\ \n [OR]  \\ MAIN.py $INPUT $CONFIG $OUTPUT \\")
        return 0

    outputFile = "Output.txt"
    
    if(len(sys.argv) == 4):
        outputFile = sys.argv[3]
        
    try:
        CHECK(sys.argv[1], sys.argv[2])
        
        CONFIGARRAY = CONFIG(sys.argv[2])
        READIN(sys.argv[1],CONFIGARRAY, outputFile)
        print ("Process complete.\nOutput in file: " + outputFile)

    except FileNotFoundError:
        print ("One or more files are not valid files.\nCheck if files exist.")
        return 1
    except ValueError:
        print ("One or more files are empty files.\nCheck if files exist and are in utf-8.")
        return 2
    except UnicodeDecodeError:
        print ("This program only decodes utf-8.\nCheck if files are in utf-8.")
        return 3



  
########################## 

main(sys.argv)
