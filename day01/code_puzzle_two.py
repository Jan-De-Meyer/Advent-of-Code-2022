with open("values.txt") as file:
    list = [0,0,0]
    temp_weight = 0
    for line in file:
        if line  == "" or line == "\n":
            list.append(temp_weight)
            temp_weight = 0
        else:
            temp_weight += int(line)
list = sorted(list)
print(list[-1]+list[-2]+list[-3])