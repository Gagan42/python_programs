n = int(input())
second_max=[]
# arr = map(int, input().split())
print(n)
arr=list(map(int,input().strip().split()))[:n] 
i=0
while i <n:
    if arr[i]<max(arr):
        second_max.append(arr[i])
    i=i+1
print(max(second_max))    
