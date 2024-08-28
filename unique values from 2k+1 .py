# here is the code for finding value in list which is onw time
#if the other values are 2(n) times
l = [1,4,5,6,5,4,8,9,7,7,8,9,1]
res = 0
for i in l:
    res = res ^ i
print(res)
