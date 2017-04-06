
# Author: Han Zhang
# This program takes in an input txt word file
# and runs a word frequency function. The program
# outputs the frequency dictionary to the user.

import codecs

def main():
    
    openfile = input("Enter a file that you want analize: ")
    words = {}

    # In case user omits the .txt suffix
    if ".txt" not in openfile:
        openfile = openfile+".txt"

    # Attempt to open the file
    try:
        file = open(openfile,"r")
    except:
        print("No such a file exists")
        quit()
    finally:
        print("Successfully accessed the file")
        
    # Characters which are acceptable as keys 
    needchr1="ABCDEFGHIJKLMNOPQRSTUVWXYZ'"
        
    # Replacing the punctuation with spaces 
    for line in file:
        text = line.rstrip('\n')
        text = text.upper()
        for w in text:  
            if w.isalpha() == False:
                if w not in needchr1:
                    text = text.replace(w," ")
        listOfWords = text.split()
        for w in listOfWords:                
            words[w] = words.get(w,0)+1                  

    #Asking the user for tivial word uses and which words do they consider trivial
    choice = input("Do you want to omit 'trivial' words (y or n)?")
    while choice != "y" and choice != "n":
        print("Please enter a valid input!")
        choice=input("Do you want to omit 'trivial' words (y or n)?") 
    
    if choice == "y":
        triv=input("Enter words you consider trivial (seperate them with a comma): ")
        triv=triv.upper()
        trivial=triv.split(",")
        for w in list(words):
            if w in trivial:
                words.pop(w)
                
    #Printing words with a specific length 
    choice2=input("Do you want to words with specific length(y or n)?")
    while choice2 != "y" and choice != "n":
        print("Please enter a valid input!")
        choice2=input("Do you want to words with specific length(y or n)?")
    keyList = list(words.keys())
    
    if choice2 == "y":
        length=int(input("Enter the word length: "))
        for i in keyList:
            if len(i) != length:
               words.pop(i)
        keyList = list(words.keys())
        keyList.sort()
        print("") 
        print("Here is a word frequency breakdown...")
        print('')
        for j in keyList:
            print(format(j,'20s'),format(words[j],'5d'))
        print("\n")
        print('')
    else:
        keyList.sort()
        print("") 
        print("Here is a word frequency breakdown...")
        print('')
        for k in keyList:
            print(format(k,'20s'),format(words[k],'5d'))
        print("\n")
        print('')

    ##Determining the mood of the text by tallying synonyms of happy and sad
    file=codecs.open("Roget_Thesaurus.txt",'r','utf-8')
    thesaur={}
    for line in file:
        line=line.rstrip("\n")
        newline=line.split(",")
        thesaur[newline[0]]=newline[1:]
    thenewkeys=list(thesaur)
    happy=thesaur["happy"]
    sad=thesaur["sad"]

    happycount=0
    sadcount=0
                  
    for i in keyList:
        if i in happy:
            happycount += words[i]
        elif i in sad:
            sadcount += word[i]
        else:
            None
    if happycount > sadcount:
        print("The overall mood of the text is positive.")
    elif happycount < sadcount:
        print("The overall mood of the text is negative.")
    else:
        print("The overall mood of the text is neutral.")

    #Unfortunately the synonyms in the given thesaurus is too limited, this is why the mood is always neutral :(

    file.close()
main()
