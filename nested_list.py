


matrix = [] 
i = int(input())
j = int(input())
k = int(input())
n = int(input())
for x in range(i+1):
    for y in range(j+1):
        for z in range(k+1):
            if ((x+y+z)!=n):
                matrix.append([x,y,z])
print(matrix)
