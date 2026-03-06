from time import time

with open("data1.txt", "r") as file:
    rawdata:str = file.read()
    data:list[str] = rawdata.split("\n")

position:int = 50
zero_counter=0

t_1=time()

for instruction in data:
    if instruction[0]=="R":
        position += int(instruction[1:])
        position %=100
    elif instruction[0]=="L":
        position -= int(instruction[1:])
        position %=100
    if position==0:
        zero_counter+=1
t_2=time()

print(f"zeroes = {zero_counter}")
print(f"time taken {int((t_2-t_1)*1000000)/1000} ms")

position:int = 50
clicks=0

t_1=time()
for instruction in data:
    if instruction[0]=="R":
        R = int(instruction[1:])
        if R>= 100-position:
            clicks += (R+position)//100
        position += R
        
    elif instruction[0]=="L":
        L = int(instruction[1:])
        if L>= position:
            if position!=0:
                clicks += (L-position)//100 + 1
            else:
                clicks += (L-position)//100
            
        position -= L
    position %= 100
t_2=time()
print(f"clicks = {clicks}")
print(f"time taken {int((t_2-t_1)*1000000)/1000} ms")