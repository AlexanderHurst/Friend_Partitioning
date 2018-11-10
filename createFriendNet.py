import random
import sys


def getBinRand(chance):
    temp = random.randint(1, 1000)
    if temp >= chance:
        return 0
    else:
        return 1


random.randint(0, 1)
list = []
n = int(sys.argv[1])
chance = int(sys.argv[2])

for i in range(n):
    list.append([getBinRand(int(chance))
                 for x in range(n)])
for i in range(len(list)):
    for j in range(len(list[i])):
        if i >= j:
            list[i][j] = 0


print("Alex Output:")
for i in list:
    print(str(i) + ",")
print("Jamie Output:")
for i in list:
    temp = ""
    for j in i:
        temp += (str(j) + " ")
    print(temp)

print("check your work")
upper = ""
for i in range(1, n+1):
    upper += (str(i) + "\t")
print("\t|\t" + upper)
print("-----------------------------------------------------------------------------------------------------------------------------------------")
for i in range(n):
    temp = ""
    for j in range(n):
        temp += (str(list[i][j]) + "\t")
    print(str(i+1) + "\t|\t" + temp)
    print()
