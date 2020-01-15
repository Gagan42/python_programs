n = int(input()) 
first_line = list(map(int,input().strip().split()))[:n] 
# input_list = input_line.split()
m = int(input()) 
second_line = list(map(int,input().strip().split()))[:m] 
# input_list = input_line.split()
cnt=0
for i in first_line:
    for j in second_line:
        if i==j:
            cnt=cnt+2
print((len(first_line)+len(second_line))-cnt)
