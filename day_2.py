from time import time
import math

with open("data2.txt", "r") as file:
    rawdata = file.read()
    data = rawdata.split(",")
    file.close()

# part 1
# def get_bins(data_line):
#     start, stop = data_line.split("-")
#     len = start.__len__()
#     stop_len = stop.__len__()
#     bins = []
#     if len==stop_len and len%2==1:
#         pass
#     else:
#         while len<=stop_len:
#             if len%2==1:
#                 len+=1
#                 s = 10**(len//2 - 1)
#             else:
#                 s = max(int(start[:len//2]) +(1 if int(start[:len//2])<int(start[len//2:]) else 0), 10**(len//2 - 1))
#                 print(10**(len//2 - 1))
                
#             if len == stop_len:
#                 e = int(stop[:stop_len//2])-(1 if int(stop[:stop_len//2])>int(stop[stop_len//2:]) else 0)
#             else:
#                 e = 10**(len//2)-1
                
#             if s>e:
#                 bin = (0,0,len//2)
#             else:
#                 bin = (s,e,len//2)
#             bins.append(bin)
#             len+=2    
        
#     return bins

# t_1=time()
# invalid_id_sum=0
# for line in data:
#     bins = get_bins(line)
#     print(line)
#     print(bins)
#     for bin in bins:
        
#         s,e,len = bin
#         invalid_id_sum+=(1+10**len)*(e**2+e-s**2+s)/2
# t_2 = time()

# print(invalid_id_sum)
# print(f"time taken {int((t_2-t_1)*1000000)/1000} ms")

# part 2
def all_divisors(n)->list:
    sqrt_n = math.sqrt(n)
    i=1
    divisors =set()
    while i<=sqrt_n:
        if n%i==0:
            divisors.add(n//i)
            divisors.add(i)
        i+=1

    divisors=sorted(list(divisors))
    return divisors

t_1=time()
invalid_id_sum_2=0
for line in data:
    # print(line)
    start,stop = line.split("-")
    num = int(start)
    stop = int(stop)
    while num<=stop:
        num_len = len(str(num))
        length_divisors = all_divisors(num_len)
        for i,l in enumerate(length_divisors[:-1]):
            b = length_divisors[-i-1]
            a=0
            for j in range(b):
                a+=10**(j*l)
                # print(j)
                # print(a)
            
                
            # print(a)
            
            
            if num%a==0:
                # print(f"num is{num}")
                invalid_id_sum_2+=num
                break
        num+=1
t_2=time()
print(invalid_id_sum_2)
print(f"time taken {int((t_2-t_1)*1000000)/1000} ms")