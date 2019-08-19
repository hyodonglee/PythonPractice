#-*- encoding: utf-8 -*-
a = []
b = []
for i in range(3):
    a.append(int(input()))

result = a[0]*a[1]*a[2]
final = str(result)
cnt = 0

for j in range(10):
    for i in range(len(final)):
        if(int(final[i]) == j):
            cnt= cnt+1
    b.append(cnt)
    cnt=0


for i in range(len(b)):
    print(b[i])