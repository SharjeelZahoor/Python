key = int(input())
lst = [2, 3, 4, 5, 6, 7, 8, 21, 34, 66]
condition = False
for i in range(lst):
    if key == i:
        condition = True
        break
    i += 1
print(condition)




