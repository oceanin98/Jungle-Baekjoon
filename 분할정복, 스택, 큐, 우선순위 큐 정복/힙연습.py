import heapq

heap=[]
heapq.heappush(heap,50)
heapq.heappush(heap,35)
heapq.heappush(heap,10)

print(heap)

heap2= [33,56,88]
heapq.heapify(heap2)

print(heap2)
result = heapq.heappop(heap)

print(result)
print(heap)