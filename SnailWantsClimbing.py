#-*- encoding: utf-8 -*-
#baekjoon 2869번

list = input().split()
A = int(list[0])
B = int(list[1])
V = int(list[2])

sum = A
day = 0

'''while(True):
    if(sum>V):
        print(day)
        break
    sum = sum + A - B
    day = day + 1'''

ExceptDay = int((V-A)/(A-B))
LastDay = int((V-A)%(A-B))

if(LastDay==0):
    day = ExceptDay + 1
else:
    day = ExceptDay + 2

print(day)

