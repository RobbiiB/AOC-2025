from time import time


with open("data2.txt", "r") as file:
    rawdata = file.read()
    data = rawdata.split(",")
    file.close()

# part 1
def get_bins(data_line):
    start, stop = data_line.split("-")
    len = start.__len__()
    stop_len = stop.__len__()
    bins = []
    if len==stop_len and len%2==1:
        pass
    else:
        while len<=stop_len:
            if len%2==1:
                len+=1
                s = 10**(len//2 - 1)
            else:
                s = max(int(start[:len//2]) +(1 if int(start[:len//2])<int(start[len//2:]) else 0), 10**(len//2 - 1))
                print(10**(len//2 - 1))
                
            if len == stop_len:
                e = int(stop[:stop_len//2])-(1 if int(stop[:stop_len//2])>int(stop[stop_len//2:]) else 0)
            else:
                e = 10**(len//2)-1
                
            if s>e:
                bin = (0,0,len//2)
            else:
                bin = (s,e,len//2)
            bins.append(bin)
            len+=2    
        
    return bins

t_1=time()
invalid_id_sum=0
for line in data:
    bins = get_bins(line)
    print(line)
    print(bins)
    for bin in bins:
        
        s,e,len = bin
        invalid_id_sum+=(1+10**len)*(e**2+e-s**2+s)/2
t_2 = time()

print(invalid_id_sum)
print(f"time taken {int((t_2-t_1)*1000000)/1000} ms")

# part 2

