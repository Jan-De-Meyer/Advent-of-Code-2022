with open("values.txt") as file:
    highest_elf = 0
    max_weight_carried = 0
    temp_weight =0
    index = 0
    for line in file:
        if line  == "" or line == "\n":
            index +=1
            if temp_weight > max_weight_carried:
                max_weight_carried = temp_weight
                highest_elf = index
                temp_weight = 0
            else:
                temp_weight = 0
        else:
            print(line)
            temp_weight += int(line)
print(max_weight_carried)