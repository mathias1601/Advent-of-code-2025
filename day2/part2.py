sum = 0

def iterateSequenzeRange(number, sequenceRange):

    startPart = 0
    endPart = sequenceRange
    sequence = str(number)[startPart:endPart]

    for i in range((len(str(number)) // sequenceRange)-1):
        
        startPart += sequenceRange
        endPart += sequenceRange

        if str(number)[startPart:endPart] != sequence:
            return 0
        
    return number

with open("input2.txt") as f:
    line = f.read()
   
    all_ranges = line.split(",")

    for numRange in all_ranges:

        rangeSplit = numRange.split("-")
        startNum = int(rangeSplit[0])
        endNum = int(rangeSplit[1])

        for number in range(startNum, endNum + 1):
            
            for sequenceRange in range(1, (len(str(number)) // 2) + 1):

                if len(str(number)) % sequenceRange == 0:
                
                    sequence = iterateSequenzeRange(number, sequenceRange)
                    
                    sum += sequence
                    
                    if sequence != 0:
                        break

                    print("---")
                    print(number)
                    print(sequence) 
                    print("---")
            
     
            
        
print(sum)

""" print(all_ranges) """