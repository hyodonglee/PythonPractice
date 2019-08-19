#-*- encoding: utf-8 -*-
#baekjoon 3052번
a = []

cnt = 0
for i in range(10):
    a.append(int(input())%42)

#print(a)

for i in range(10):
    for j in range(i+1,10):
        if(a[i]==a[j]):
            cnt = cnt-1
            break
    cnt = cnt + 1

print(cnt)