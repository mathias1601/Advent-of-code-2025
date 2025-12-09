sum = 0

with open("input2.txt") as f:
    line = f.read()
   
    all_ranges = line.split(",")

    for numRange in all_ranges:

        rangeSplit = numRange.split("-")
        startNum = int(rangeSplit[0])
        endNum = int(rangeSplit[1])

        for number in range(startNum, endNum + 1):
            
            if len(str(number)) % 2 == 0:
                mid = int(len(str(number)) / 2)
                firstHalf = str(number)[:mid]
                secondHalf = str(number)[mid:]

                if firstHalf == secondHalf:
                    sum += number

                """ print("---")
                print(number)
                print(firstHalf)    
                print(secondHalf) 
                print("---") """
            
     
            
        
print(sum)

""" print(all_ranges) """