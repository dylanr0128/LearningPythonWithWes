def printHelloWorld():

    print("learning with wes")

def printString(userEntry):

    print(userEntry)

def addNumbers(userEntryA, userEntryB):

    total = userEntryA + userEntryB
    print(total)

    addToTotal(total)

def addToTotal(total):
    
    userEntryC = int(input("Enter Number:"))

    total += userEntryC

    print(total)