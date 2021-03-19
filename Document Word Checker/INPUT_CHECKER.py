import string
import os
import sys

#############################
# Expected input:   two arguments.
# 
# Output: no output any files are not empty. If any are empty, raises a valueerror
#
# Function: Checks both files and raises an error if any are empty.
#
# (C): Yu-Dean Wang, @ 3/18/2021.
#############################
def CHECK(arg1, arg2):
        m = open(arg1, 'r', encoding = "utf-8")
        m.close()
        
        if os.stat(arg1).st_size == 0:
            raise ValueError()

        m = open(arg2, 'r', encoding = "utf-8")
        m.close()
        
        if os.stat(arg2).st_size == 0:
            raise ValueError()
            
