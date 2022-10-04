
import sys


input= sys.stdin.readline
n= int(input()) #5
m= list(map(int,input().split())) #12345
a= int(input()) #5
b=list(map(int,input().split())) #13795

m.sort() #정렬
   
def bin_search(l,m,start,end):
    if start > end:
        return 0
    a=(start+end)//2 
    if l == m[a]:
        return 1
    elif l <m[a]:
        return bin_search(l,m,start,a-1)
    else:
        return bin_search(l,m,a+1,end)

for l in b:
    start = 0
    end=len(m)-1
    
    print(bin_search(l,m,start,end))

