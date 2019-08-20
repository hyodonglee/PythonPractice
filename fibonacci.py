#-*- encoding: utf-8 -*-
#baekjoon 2748번(fibonnaci)

n = int(input())

def fib(n,a,b):
    if(n==1):
        return 1
    elif(n==0):
        return 0
    else:
        for i in range(n-1):
            tmp = a+b
            a = b
            b = tmp
    return tmp


print(fib(n,0,1))