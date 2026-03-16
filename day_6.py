import re
from time import time

with open("data6.txt","r") as file:
    rawdata=file.read()
    file.close
    datarows=rawdata.split("\n")

#part 1
t_1=time()
data=[]     
for row in datarows:
    x = re.split(" +", row)
    data.append(x)



y_max = data.__len__()
x_max = data[0].__len__()-1

total=0
for i in range(x_max):
    if data[-1][i]=="+":
        math_eq=0
        for j in range(y_max-1):
            if data[j][0] =="":
                try:
                    math_eq+=int(data[j][i+1])
                except:
                    math_eq+=0
            else:
                try:
                    math_eq+=int(data[j][i])
                except:
                    math_eq+=0
    else:
        math_eq=1
        for j in range(y_max-1):
            if data[j][0] =="":
                try:
                    math_eq*=int(data[j][i+1])
                except:
                    math_eq+=0
            else:
                try:
                    math_eq*=int(data[j][i])
                except:
                    math_eq+=0

    # print(math_eq)
    total+=math_eq
t_2=time()
print(total)
print(f"time taken {int((t_2-t_1)*1000000)/1000} ms")



t_3=time()
start_column = [m.start(0) for m in re.finditer("[*+]", datarows[-1])]
# print(start_column)
continue_loop=True
total=0
for start_ind in start_column:
    continue_loop=True
    if datarows[-1][start_ind]=="+":
        math_eq=0
        relative_postion=0
        
        while continue_loop:
            num =""
            for i in range(datarows.__len__()-1):
                num = num+ datarows[i][start_ind+relative_postion]
            if num==(datarows.__len__()-1)*" ":
                continue_loop=False
            else:
                number=int(num)
                # print(number)
                math_eq+=number
            relative_postion+=1
        # print(math_eq)
    else:
        math_eq=1
        relative_postion=0
        while continue_loop:
            num =""
            for i in range(datarows.__len__()-1):
                num = num+ datarows[i][start_ind+relative_postion]
            if num==(datarows.__len__()-1)*" ":
                continue_loop=False
            else:
                number=int(num)
                # print(number)
                math_eq*=number
            relative_postion+=1
        # print(math_eq)
    total+=math_eq
t_4=time()
print(total)
print(f"time taken {int((t_4-t_3)*1000000)/1000} ms")