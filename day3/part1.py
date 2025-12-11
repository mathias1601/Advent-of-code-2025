sum = 0

# Helper-function to loop through a number and find the greatest digit and its position
def findGreatestDigit(number):

    digit = 0
    index = 0

    for i in range(len(number)):
        newDigit = int(number[i])

        if newDigit > digit:
            digit = newDigit
            index = i

    return digit, index + 1


with open("input3.txt") as f:

    for bankLine in f:
        
        bankLine = bankLine.strip("\n")

        # using bankline[:-1] to remove the last digit of the string, this is beacuse the first digit cannot be the last one in the line
        firstDigit, index1 = findGreatestDigit(bankLine[:-1])
        secondDigit, index2 = findGreatestDigit(bankLine[index1:])

        sum += int(str(firstDigit) + str(secondDigit))


print(sum)
        
