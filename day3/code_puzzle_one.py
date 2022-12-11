import string
#yea fuck typing all that out
priorities = list(string.ascii_lowercase + string.ascii_uppercase) 
total = 0
with open("values.txt") as file:
     for line in file:
        first_half =line[0:(int(len(line)/2))]
        second_half = line[(int(len(line)/2)):]
        for item in first_half:
            for item2 in second_half:
                if item == item2:
                    to_add= priorities.index(item)+1
        total += to_add
        
print(total)