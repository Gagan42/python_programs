
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
   
    scores = list(map(float, line))
    # print(scores)
    student_marks[name] = scores
    
query_name = input()
b=0
for key,value in student_marks.items() :
    if key==query_name:
        value_lenghth=len(value)
        inner_value=value
        for i in inner_value :
            # print(float(i))
           b=b+float(i)
        b=round(b/value_lenghth,2)   
print(format(b, '.2f'))

