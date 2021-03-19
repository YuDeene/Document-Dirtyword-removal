import re
import string

#############################
# Expected input:   config file, a file.
#   Expects the file to be in format: REGEX \n REGEX \n REGEX
#
#
# Output: m, an array of words.
#
# Function: Takes a file and places all words into an array.
#
# (C): Yu-Dean Wang, @ 3/18/2021.
#############################
def CONFIG(Configfile):
    CONFIG = open(Configfile, 'r', encoding = "utf-8")
    m = []
    fileNotEnd = True
    while fileNotEnd:
        line = (CONFIG.readline())
        if not line:
           fileNotEnd = False
        else:
            m.append(line.rstrip())
    CONFIG.close()
    return m
