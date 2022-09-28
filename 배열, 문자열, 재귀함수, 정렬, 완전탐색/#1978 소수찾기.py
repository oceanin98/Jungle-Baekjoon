a= int(input())#주어진N개 
num = list(map(int, input().split()))
sosu = 0
for i in num:
    error = 0
    if i >1:
        for _ in range(2, i): 
            if i % _ ==0:
                error += 1
            if error == 0:
                sosu += 1
print(a)
