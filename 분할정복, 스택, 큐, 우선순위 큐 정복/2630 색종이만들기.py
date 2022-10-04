from numpy import busday_count


def makepaper(x,y,n):
    global wcount,bcount
    color = paper[x][y]
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                makepaper(x,y,n//2)
                makepaper(x,y+n//2,n//2)
                makepaper(x+n//2,y,n//2)
                makepaper(x+n//2,y+n//2,n//2)
                return
            

    if color == 0:
        wcount +=1
    else:
        bcount +=1
    
if __name__ =="__main__":
    n= int(input())
    paper = [list(map(int,input().split())) for _ in range(n)]
    wcount, bcount = 0,0
    
    makepaper(0,0,n)
    print(wcount)
    print(bcount)
