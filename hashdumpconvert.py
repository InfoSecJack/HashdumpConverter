#Python hashdump converter
#Free to use, too simple to care
#Please name input file as 'input.txt'
#Outputted file is called 'output.txt'

def filter(inputstr): #used to get rid of the middle stuff

    subreturn = ""  

    #gets the substring before the first ':' which is usually the username
    subreturn += inputstr[:inputstr.index(":")] 

    #gotta have that ':'
    subreturn += ":"

    #reverses the string, gets the first ':', splits it, and then reverses it
    subreturn += inputstr[::-1][:inputstr[::-1].index(":")][::-1]

    return subreturn


def openFile():

    with open("input.txt") as f:

        return f.readlines()


def main():

    with open("output.txt", "w") as f:

        for x in openFile():

            f.write(filter(x))

if __name__ == "__main__":
    
    main()
