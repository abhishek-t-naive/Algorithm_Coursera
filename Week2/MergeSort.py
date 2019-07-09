# Implementation of Merge-Sort algorithm using Divide and Conquer paradigm

# Reading the unsorted array from a file into a list
filename = 'test.txt'

array = [line.rstrip('\n') for line in open(filename)]
array = [int(i) for i in array]
print(array)
#array = [1, 3, 5, 7, 4, 6, 8, 2, 19, 15, 12, 11, 16, 17, 10, 20]
 
 
#function for dividing and calling merge function
def Mergesort(array):
  n = len(array)
  if(n<2):
    return
 
  mid = n/2
  left = []
  right = []
  
  for i in range(mid):
    number = array[i]
    left.append(number)  
   
  for i in range(mid,n):
    number = array[i]
    right.append(number)
 
  Mergesort(left)
  Mergesort(right)
 
  Merge(left,right,array)
 
def Merge(left, right, array):
	i = 0
	j = 0
	#k = 0

	print'Merging!'
	print(array)
	print(left)
	print(right)

	
	for k in range(len(array)):
		if (i<len(left) and j<len(right)):
			print('value of i is ',i, 'value of j is', j)
			print('Entering first while statement')
			if(left[i] < right[j]):
				print('Left index value is ', left[i], 'Right index value is ', right[j])
				array[k] = left[i]
				print('Value is being entered at index ', k, 'and the value is', array[k])
				print('End of iteration ', i, j)
				i = i+1
			else:
				print('Entering the else of first while statement')
				print('Left index value is ', left[i], 'Right index value is ', right[j])
				array[k] = right[j]
				print('Value is being entered at index ', k, 'and the value is', array[k])
				print('End of iteration ', i, j)
				j = j+1
		elif(i<len(left)):
			print('Entering second while statement')
			print('Left index value is ', left[i])
			array[k] = left[i]
			print('Value is being entered at index ', k, 'and the value is', array[k])
			i = i+1
		else:
			print('Entering third while statement')
			print('Right index value is ', right[j])
			array[k] = right[j]
			print('Value is being entered at index ', k, 'and the value is', array[k])
			j = j+1
	print('Merging done! Sorted array is ',array)

#calling Mergesort
Mergesort(array)
for i in array:
  print i,
