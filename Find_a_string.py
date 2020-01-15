# import json
# string = input().strip()
# sub_string = input().strip()
# z=list()
# count=0
# len_sub_string=len(sub_string)
# for j in range(0,len(string)):
# 	z=[string[j:j+len(sub_string)]]
# 	res = ''.join(z) 
# 	# print(res)
# 	if(sub_string==res):
# 		count=count+1
# print(count)
		
# 	# j=count


def count_substring(string, sub_string):
	z=list()
	count=0
	len_sub_string=len(sub_string)
	for j in range(0,len(string)):
		z=[string[j:j+len(sub_string)]]
		res = ''.join(z) 
		# print(res)
		if(sub_string==res):
			count=count+1

	return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)