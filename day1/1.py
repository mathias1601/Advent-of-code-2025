dial = 50

times_on_zero = 0

with open("input1.txt") as f:
    for line in f:
        direction, steps = line.strip()[0], int(line.strip()[1:])
        if direction == "L":
            if dial == 0:
                times_on_zero -= 1

            temp_dial = (dial - steps) % 100
            times_on_zero += -((dial - steps) // 100)
            dial = temp_dial

            if dial == 0:
                times_on_zero += 1

        elif direction == "R":
            temp_dial = (dial + steps) % 100
            times_on_zero += (dial + steps) // 100
            dial = temp_dial
        

        """ print("---")
        print(dial)
        print(times_on_zero)
        print("---") """

print(times_on_zero)