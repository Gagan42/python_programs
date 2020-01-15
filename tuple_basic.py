# n = int(input("Enter number of elements : ")) 
  
# # Below line read inputs from user using map() function 
# i=0 
# while i<n:
#     a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n] 
#     print("\nList is - ", a) 
#     i=i+1

n = int(input()) 
input_line = list(map(int,input().strip().split()))[:n] 
# input_list = input_line.split()
input_list = map(int, input_line)    
t = tuple(input_list)
print(hash(t))   