# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")
    answer = 'yes'
    while answer == 'yes':
        ask()
        option = input("Enter menu selection (1-5): ")
    
        if option == '1':
            word = input("Please enter a word: ").lower()
            index = linearSearch(dictionary, word)
            print("Linear Search starting...")
            initial_time = time.time()

            if index != -1:
                total_time = time.time() - initial_time
                print(word + " is IN the dictionary at position " + str(index))
                print (str(total_time) + " seconds")
            else: 
                total_time = time.time() - initial_time
                print(word + " is NOT IN the dictionary ")
                print (str(total_time) + " seconds")

        elif option == '2':
            word = input("Please enter a word: ").lower()
            index = binarySearch(dictionary, word)
            print("Binary Search starting...")
            initial_time = time.time()
            if index != -1:
                total_time = time.time() - initial_time
                print(word + " is IN the dictionary at position " + str(index))
                print(str(total_time) + " seconds")
                
            else: 
                total_time = time.time() - initial_time
                print(word + " is NOT IN the dictionary ")
                print(str(total_time) + " seconds")

        elif option == '3':
            gone = 0
            print("Linear Search starting...")
            initial_time = time.time()
            for i in range(len(aliceWords)):
                index = linearSearch(dictionary, aliceWords[i].lower())
                if index == -1:
                    gone += 1 
            print("Number of words not found in dictionary: " + str(gone))
            total_time = time.time() - initial_time
            print(str(total_time) + " seconds")

        elif option == '4':
            gone = 0
            print("Binary Search starting...")
            initial_time = time.time()
            for i in range(len(aliceWords)):
                index = binarySearch(dictionary, aliceWords[i].lower())
                if index == -1:
                    gone += 1 
            print("Number of words not found in dictionary: " + str(gone))
            total_time = time.time() - initial_time
            print(str(total_time) + " seconds")
        elif option == "5":
            print("See you later")
            answer = 'no'
        

def ask():
    print ("Main Menu")
    print ("1: Spell Check a Word (Linear Search)")
    print ("2: Spell Check a Word (Binary Search)")
    print ("3: Spell Check Alice In Wonderland (Linear Search)")
    print ("4: Spell Check Alice In Wonderland (Binary Search)")
    print ("5: Exit")


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()


# Spell Check Assignment

# My linear and binary seaches

import math

def linearSearch(anArray, item):
    for i in range(len(anArray)) :
        if anArray[i] == item :
            return i
    return -1



def binarySearch(anArray, item) :
    lower_index = 0
    upper_index = len(anArray) - 1

    while lower_index <= upper_index :
        mid = math.floor((lower_index + upper_index) / 2)
        if (item == anArray[mid]):
            return mid
        elif (item < anArray[mid]):
            upper_index = mid - 1
        else :
            lower_index = mid + 1
        
    return -1


# Call main() to begin program
main()