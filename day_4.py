from time import time


with open("data4.txt", "r") as file:
    rawdata = file.read().split("\n")
    data = []
    for row in rawdata:
        data.append(list(row))


y_range= len(data)
x_range= len(data[0])

def check_around(data,y,x,y_range,x_range):
    min_y=max(0,y-1)
    max_y=min(y_range-1,y+1)
    min_x=max(0,x-1)
    max_x=min(x_range-1,x+1)
    locs = [(min_y,min_x), (min_y,x), (min_y,max_x),
            (y,min_x), (y,x), (y,max_x),
            (max_y,min_x), (max_y,x), (max_y,max_x)]
    
    locs = list(set(locs))
    # print(locs)
    i=0
    for loc in locs:
        if data[loc[0]][loc[1]]=="@":
            i+=1
        if i>4:
            return False
    return True
    pass
    
#part1
t_1=time()
num=0
for y in range(y_range):
    for x in range(x_range):
        if data[y][x]=="@":
            if check_around(data,y,x,y_range,x_range):
                num +=1
t_2=time()
print(num)
print(f"time taken {int((t_2-t_1)*1000000)/1000} ms")

#part2
t_3=time()
num1=0
while True:
    
    num2=0
    for y in range(y_range):
        for x in range(x_range):
            if data[y][x]=="@":
                if check_around(data,y,x,y_range,x_range):
                    num2 +=1
                    data[y][x]="X"
    num1= num1+num2
    if num2==0:
        break
t_4=time()

print(num1)
print(f"time taken {int((t_4-t_3)*1000000)/1000} ms")
