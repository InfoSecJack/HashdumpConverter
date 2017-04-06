#Python hashdump converter V1.3
#By Jack Alston
#Free to use, too simple to care
#When used with hashcat be sure to include '--username'

#This is shown when the user does "-h"
help ="""
Python Hashdump converter.

Usage:
  hashdumpconvert.py
  hashdumpconvert.py -h
  hashdumpconvert.py -i <input file>
  hashdumpconvert.py -i <input file> -o <output file>
  hashdumpconvert.py -o <output file>
  hashdumpconvert.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
"""

import sys


def checkargs():

    if "--version" in sys.argv:
        print("\nVersion 1.3 \n06/04/2017")
        exit()

    if "-h" in sys.argv:
        print(help)
        exit()
    
    if "-i" in sys.argv:
        filename = sys.argv[sys.argv.index("-i") + 1]
    else:
        filename = "input.txt"

    if "-o" in sys.argv:
        outfilename = sys.argv[sys.argv.index("-o") + 1]
    else:
        outfilename = "output.txt"

    return filename, outfilename

def filterstr(inputstr): #Used to get rid of the middle stuff

    inputstr = inputstr.strip(":")

    substring = "{}:{}".format(
        inputstr[:inputstr.index(":")],
        inputstr[inputstr.rindex(":"):]
        )
    
    return substring


def openFile(): #Used to open the input file for iteration

    with open(filename) as f:

        return f.readlines()


def main():

    with open(outfilename, "w") as f:

        for x in openFile():

            f.write(filterstr(x))

if __name__ == "__main__": #More of a habit now, purely optional

    filename, outfilename = checkargs()
        
    main()
