def linearSearch(anArray, item):
    for i in range(len(anArray)) :
        if anArray[i] == item :
            return i
    return -1

nums = [10, 30, 40, 45, 70, 80, 85, 90, 100];
words = ["at", "ball", "cat", "dog", "eye", "fish", "good"];
unsorted = [30, 20, 70, 40, 50, 100, 90];

print(linearSearch(nums, 100));
print(linearSearch(nums, 75));
print(linearSearch(words, "fish"));
print(linearSearch(words, "at"));
print(linearSearch(unsorted, 70));

import math

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
            
            
nums = [10, 30, 40, 45, 70, 80, 85, 90, 100]
words = ["at", "ball", "cat", "dog", "eye", "fish", "good"]
unsorted = [30, 20, 70, 40, 50, 100, 90]
 
print(binarySearch(nums, 100))
print(binarySearch(nums, 75))
print(binarySearch(words, "fish"))
print(binarySearch(words, "at"))
print(binarySearch(unsorted, 70))

