import string
#yea fuck typing all that out
priorities = list(string.ascii_lowercase + string.ascii_uppercase) 
total = 0
group = []
with open("values.txt") as file:
    for _ in range(1,100):
        for x in range(1,3):
            print(file.readlines(_*x))