from numpy import busday_count

# 아에반듯 
def makepaper(x,y,n):
    global wcount,bcount
    color = paper[x][y]
    
    #이중 for문으로 i와 j로 paper의 행, 열 인덱스를 접근하면서 해당 인덱스의 좌표 색을
    #아까 저장해놓은 가장자리 색과 같은지 비교하고 다를경우 종이 가로 세로 쪼개기를 해준다 
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                makepaper(x,y,n//2)
                makepaper(x,y+n//2,n//2)
                makepaper(x+n//2,y,n//2)
                makepaper(x+n//2,y+n//2,n//2)
                return
            
            
            
            
            
#종료조건 : 모두 같은 색 , 하나의 정사각형 될경우

#하얀색 0 , 파란색 1
#
    if color == 0:
        
        wcount +=1
        
    else:
        bcount +=1

if __name__ =="__main__":
    n= int(input())
    paper = [list(map(int,input().split())) for _ in range(n)]
    wcount, bcount = 0,0
    
    makepaper(0,0,n)
    #하얀색 색종이 수
    print(wcount)
    #파란색 색종이 수 
    print(bcount)
