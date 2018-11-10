import random
import sys


def getBinRand(chance, out_of):
    temp = random.randint(1, out_of)
    if temp > chance:
        return 0
    else:
        return 1


random.randint(0, 1)
list = []
n = int(sys.argv[1])
chance = int(sys.argv[2])
out_of = int(sys.argv[3])

for i in range(n):
    list.append([getBinRand(chance, out_of)
                 for x in range(n)])
for i in range(len(list)):
    for j in range(len(list[i])):
        if i >= j:
            list[i][j] = list[j][i]
temp = ""
for i in list:
    temp += (str(i) + ",\n")
temp = temp[:-2]
print(temp)

print("\ncheck your work")
upper = ""
for i in range(1, n+1):
    upper += (str(i) + "\t")
print("\t|\t" + upper)
horiz = ""
for i in range(0, n+2):
    horiz += "-\t"
print(horiz)
for i in range(n):
    temp = ""
    for j in range(n):
        temp += (str(list[i][j]) + "\t")
    print(str(i+1) + "\t|\t" + temp)
    print()
