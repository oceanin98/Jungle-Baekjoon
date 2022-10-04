#입력했을떄 마지막
#스택을 이용한 역순 출력
class stack:
    def __init__(self):
        self.top=[]
    def isEmpty(self): return len(self.top)==0
    def size(self):return len(self.top)
    def clear(self): self.top=[]
    
    def push(self,item):
        self.top.append(item)
        
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
        
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
        
    def __str__(self):
        return str(self.top[::-1])

stackA=stack()
string= str(input('단어를 입력하세요'))
lenstring=len(string)

for i in range(0, lenstring):
    stackA.push(string[i])
    
print("역순으로 출력",end='')
for i in range(2,lenstring):
    print(stackA.pop(), end='')

print(stackA)