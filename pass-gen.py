import random
ch_low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ch_up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
sym = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
password = ""
passList=[]
random.shuffle(ch_low)
random.shuffle(ch_up)
random.shuffle(sym)
for i in range(3):
    x=random.choice(ch_low)
    passList.append(x)
for i in range(3):
    x=random.choice(ch_up)
    passList.append(x)
for i in range(3):
    x=random.choice(sym)
    passList.append(x)
for i in range(3):
    x=random.randint(1,9)
    passList.append(x)
random.shuffle(passList)
for i in range(len(passList)):
    password+=str(passList[i])
print(password)
    