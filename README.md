# Document-Dirtyword-removal
Source code and executable for removing targeted words in a document, using python.


Outline:
This program will take an input document, and remove all words that are in the config files. The config file can use regular expressions.
It will place the output in a file given by the user, or "Output.txt" if a filename was not specified.

Depends on python libraries: sys, getopt, re, string, os

How to compile:
Make sure CONFIG_PROCESSOR, INPUT_CHECKER, INPUT_PROCESSOR, and MAIN are in the same folder.

Using pyinstaller, use the command:

pyinstaller --onefile MAIN.py.

Then a folder called Dist will be created, where MAIN.exe will be located.

How to run:
Put Input and Config files in the same folder as MAIN.exe.
Both files must be in UTF-8.

Commands: MAIN.py $INPUT $CONFIG 
	  MAIN.py $INPUT $CONFIG $OUTPUT

If using Python, make sure CONFIG_PROCESSOR, INPUT_CHECKER, INPUT_PROCESSOR, and MAIN are in the same folder.

Output will be overwritten, and in UTF-8.
