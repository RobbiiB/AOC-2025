from time import time

with open("data5.txt", "r") as file:
    fresh_ranges,ingredient_ids=file.read().split("\n\n")
    fresh_ranges = fresh_ranges.split("\n")
    ingredient_ids = ingredient_ids.split("\n")
    file.close()

t_1=time()

ranges=[]
for fresh_range in fresh_ranges:
    s,e = fresh_range.split("-")
    s=int(s)
    e=int(e)
    ranges.append([s,e])
ranges.sort(key=lambda x: x[0])

i=0
while i <len(ranges)-1:
    if ranges[i+1][0]<=ranges[i][1] and ranges[i+1][1]>ranges[i][1]:
        ranges[i][1] = ranges[i+1][1]
        ranges.pop(i+1)
    elif ranges[i+1][0]>ranges[i][1]:
        i+=1
        pass
    else:
        ranges.pop(i+1)
#part 1
# t_1=time()
fresh_id_num=0
for id in ingredient_ids:
    id= int(id)
    for range in ranges:
        start,stop=range
        if id>=start and id<=stop:
            fresh_id_num+=1
            break
t_2=time()
print(fresh_id_num)
print(f"time taken {int((t_2-t_1)*1000000)/1000} ms")
#part 2
t_3=time()

total_fresh_ids=0
for range in ranges:
    total_fresh_ids+= range[1]-range[0]+1
t_4=time()

print(total_fresh_ids)
print(f"time taken {int((t_4-t_3)*1000000)/1000} ms")    


