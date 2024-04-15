#Lab 1

from functools import *

def SumEvenNumbers(value: int, logging: bool = False):
    filtered = list(filter(lambda x: x % 2 == 0, value))
    squared = list(map(lambda x: x**2, filtered))
    result = reduce(lambda x, y:  x + y, squared)

    #print("--- SumEventNumbers logging ---")
    #print("Filtered list: " + str(filtered))
    #print("Squared list: " + str(squared))
    #print("Result: " + str(result))
    #print("--- Ending ---")

    if logging != True:
        return result

    LogFunctionData("SumEvenNumbers", "Filtered list: ", filtered)
    LogFunctionData("SumEvenNumbers", "Squared list: ", squared)
    LogFunctionData("SumEvenNumbers", "Result: ", result)

    return result

def LogFunctionData(tag: str, messege: str, value):
    print(f"Log[{tag}]\t" + messege + str(value))

nums = [ 1, 2, 3, 4, 5, 6, 7, 8 ]

print(SumEvenNumbers(nums, True))
