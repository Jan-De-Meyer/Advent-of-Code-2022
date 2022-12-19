with open("values.txt") as file:
        first_elf = []
        second_elf = []
        for line in file:
            x = line.split(",")
            first_elf.append(x[0])
            second_elf.append(x[1])
            templist = []
        for _ in first_elf:
            x = _.split("-")
            templist.append(list(map(int, x)))
        first_elf = templist
        templist= []
        for _ in second_elf:
            x = _.split("-")
            templist.append(list(map(int, x)))
        second_elf = templist
        counter = 0
        for _ in first_elf:
            index = first_elf.index(_)
            if (_[0] >= second_elf[index][0] and _[1] <= second_elf[index][1]) or (_[0] <= second_elf[index][0] and _[1] >= second_elf[index][1]):
                    counter += 1
        print(len(first_elf))
        print(counter)
            
        
