#-*- encoding: utf-8 -*-
#baekjoon 1920번(binary search)
import sys

def binarySearch(i,start,end):
    while(start<=end):
        mid = (start + end) // 2
        if(b[i]==a[mid]):
            return 1
        elif(b[i]<a[mid]):
            end = mid-1
        else:
            start = mid+1
    return 0

a=list()
b=list()

'''n = int(input())
aL = input().split(" ")
aL.sort()
for i in range(n):
  a.append(int(aL[i]))

m = int(input())
bL = input().split(" ")
for i in range(n):
    b.append(int(bL[i]))'''
#print(a)
#print(b)

n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
a.sort()

for i in range(m):
    print(binarySearch(i,0,n-1))