#Python hashdump converter V1
#By Jack Alston
#Free to use, too simple to care
#Please name input file as 'input.txt'
#Outputted file is called 'output.txt'
#When used with hashcat be sure to include '--username'

def filter(inputstr): #Used to get rid of the middle stuff

    subreturn = ""  

    #Gets the substring before the first ':' which is usually the username
    subreturn += inputstr[:inputstr.index(":")] 

    #Gotta have that ':'
    subreturn += ":"

    #Reverses the string, gets the first ':', splits it, and then reverses it
    subreturn += inputstr[::-1][:inputstr[::-1].index(":")][::-1]

    return subreturn


def openFile(): #Used to open the input file for iteration

    with open("input.txt") as f:

        return f.readlines()


def main():

    with open("output.txt", "w") as f:

        for x in openFile():

            f.write(filter(x))

if __name__ == "__main__": #More of a habit now, purely optional
    
    main()
