sum = 0

# Helper-function to loop through a number and find the greatest digit and sliced up version of the original number
# OriginalNumber is the non-shortened number which is returned sliced
def findGreatestDigit(number, originalNumber):

    digit = int(number[0])
    index = 0

    for i in range(len(number)):
        newDigit = int(number[i])

        if newDigit > digit:
            digit = newDigit
            index = i

    return digit, originalNumber[index + 1:]


with open("input3.txt") as f:

    for bankLine in f:
        
        bankLine = bankLine.strip("\n") 

        allDigits = ""

        for i in reversed(range(0, 12)):
            # Edge case for slicing. list[:0/-0] returns an empty string
            if i == 0:
                newDigit, bankLine = findGreatestDigit(bankLine, bankLine)
            else:
                newDigit, bankLine = findGreatestDigit(bankLine[:-i], bankLine)
            
            allDigits += str(newDigit)
        
        sum += int(allDigits)


print(sum)
        
