from time import time

with open("data3.txt", "r") as file:
    data = file.read().split("\n")

t_1=time()
sum = 0
for row in data:
    row = list(row)
    num1=0
    num2=0
    for i,digit in enumerate(row):
        if int(digit)>num1 and i+1!=len(row):
            num1=int(digit)
            num2=0
        elif int(digit)>num2:
            num2=int(digit)
        
    sum += 10*num1+num2
t_2=time()
# print(sum)

# t_1=time()
# sum=0  
# for row in data:
#     row = list(row)
#     nums=[0,0,0,0,0,0, 0,0,0, 0,0,0]

#     for i,digit in enumerate(row):
#         dig = int(digit)
#         for j,num in enumerate(nums):
#             # print(dig)
#             if num<dig and i<=len(row)-12+j:
#                 nums[j]=dig
#                 for k in range(11-j):
#                     nums[k+j+1]=0
#                 break
#     for i in range(12):
#         sum+= nums[::-1][i]*10**i
# t_2=time()

print(f"time taken {int((t_2-t_1)*1000000)/1000} ms")


print(sum)

