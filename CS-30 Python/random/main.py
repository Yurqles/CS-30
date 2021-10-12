# def fahrToCelsius(fahrTemp):
#     answer = int((fahrTemp - 32) * 5/9)
#     return answer

# print(fahrToCelsius(32))
# print(fahrToCelsius(68))
# print(fahrToCelsius(5))

# def analyzeNumber(aNumber):
#     if(aNumber < 0) : 
#         return "negative"
#     elif(aNumber > 0) :
#         return "positive"
#     else:
#         return "Zero"
# print(analyzeNumber(23))
# print(analyzeNumber(-300))
# print(0)

# def analyzeList(aList): 
#     print (len(aList))
#     print (aList[0])
#     print (aList[(len(aList) - 1)])

# analyzeList(["a", "b", "c", "d"])

# def countItems(anItem, aList) :
#     ComprehensiveTotal = 0
#     for x in aList:
#         if x == anItem:
#             ComprehensiveTotal += 1
    
#     return ComprehensiveTotal


# idk is going on here
# def replaceAll(oldVal, newVal, aList) :
#     for i in range(len(aList)) :
#         if aList[i] == oldVal:
#             aList[i] = newVal
            

# myList = [1, 2, 3, 1, 2, 3]
# replaceAll(1, 5, myList)
# print(myList)

def swap(index1, index2, aList):
    replace1 = aList[index1]
    replace2 = aList[index2]
    aList[index2] = replace1
    aList[index1] = replace2


myList = ["a", "b", "c", "d"]
swap(0, 2, myList)
print (myList)



# def createRandomList(n, low, high) :
#     import random
#     array = []
#     i = 0
#     while i < n :
#         array.append(random.randint(low, high))
#         i += 1
    
#     return array

# myRandomList = createRandomList(10, 1, 6)
# print(myRandomList)


