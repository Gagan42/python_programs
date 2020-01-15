import numpy


# my_array = numpy.array([[1,2,3],
#                         [4,5,6]])
# print (numpy.transpose(my_array))
# print (my_array.flatten())

n, m = map(int, input().split())
array = numpy.array([input().strip().split() for _ in range(n)], int)
print (array.transpose())
print (array.flatten())