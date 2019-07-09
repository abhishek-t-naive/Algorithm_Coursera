#Implementation of Count-Inversion algorithm using Divide and Conquer paradigm from course Design and Analysis of Algorithms I

# Reading the unsorted array from a file into a list
filename = 'Integer.txt'

array = [line.rstrip('\n') for line in open(filename)]
array = [int(i) for i in array]
print(array)
#array = [1, 3, 5, 7, 4, 6, 8, 2, 19, 15, 12, 11, 16, 17, 10, 20]
 
def Sort_and_count(array):
	length = len(array)
	if length == 1:
		return 0
	else:
		leftArray		= array[:length/2]
		rightArray	= array[length/2:]

		invLeft		= Sort_and_count(leftArray)
		invRight	= Sort_and_count(rightArray)
		invSplit	= Count_Split_Inv(array,leftArray,rightArray)
		return (invLeft+invRight+invSplit)


def Count_Split_Inv(array,left,right):
	i = 0
	j = 0
	invSplit = 0	

	print'Counting Split Inversions!'
	
	for k in range(len(array)):
		if (i<len(left) and j<len(right)):
			if(left[i] < right[j]):
				array[k] = left[i]
				i = i+1
			else:
				array[k] = right[j]
				invSplit = invSplit + len(left) - (i)
				j = j+1
		elif(i<len(left)):
			array[k] = left[i]
			i = i+1
		else:
			array[k] = right[j]
			j = j+1
	print('Counting done!')
	return invSplit

#calling Sort_and_count
inversions = Sort_and_count(array)
print inversions
