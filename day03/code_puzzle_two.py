import string
#not finished all garbage dont judge
#yea fuck typing all that out
priorities = list(string.ascii_lowercase + string.ascii_uppercase) 
total = []
group = []

compare1 = False
compare2 = False
with open("values.txt") as file:
    for _ in range(1,300):
        if len(group) < 3:
            group.append(file.readlines(_))
        else:
            for x1 in group[0]:
                for x in x1:
                    for y1 in group[1]:
                        for y in y1:
                            if x == y:
                                compare1 = True
                                for z1 in group[2]:
                                    for z in z1:
                                        if z == x:
                                            compare2 = True
        if compare1 == True and compare2 == True:
            total.append(x)
        group = []
                        
    print(len(total))