# Implementation of Quick-Sort algorithm in Python as taught in the course: Design and Analysis of Algorithms on Coursera

def QuickSort(array, low, high,flag):
	if(low<high):	
		length = high-low
		
		ChoosePivot(array,low,high,flag)
		
		pivotIndex = Partition(array,low,high)
	
		leftComparisons		= QuickSort(array,low,pivotIndex-1,flag)
		rightComparisons	= QuickSort(array,pivotIndex+1,high,flag)
	
		#NOTE: I am using 'length', not 'length-1' as it is zero indexed and I am already passing 'length-1' to the QuickSort function	
		return leftComparisons+rightComparisons+length
	else:
		return 0

# NOTE: flag 0: choose first element as pivot
#				flag 1: choose last element as pivot
#				flag 2: choose median element as pivot
def ChoosePivot(array,low,high,flag):
	if (flag == 0):
		Swap(array,low,low)
	elif(flag == 1):
		Swap(array,low,high)
	else:
		if((high-low+1)%2 == 0):
			middleIndex = (high-low+1)//2 - 1
		else:
			middleIndex = (high-low+1)//2
		middle = low + middleIndex
		middleElem = array[middle]
		ChooseMedian(array,low,middle,high)

def ChooseMedian(array,low,middle,high):
	if((array[middle] >= array[low] and array[middle] <= array[high]) or (array[middle] <= array[low] and array[middle]>= array[high])):
			Swap(array,low,middle)
	elif((array[high] >= array[middle] and array[high] <= array[low]) or (array[high] <= array[middle] and array[high]>= array[low])):
			Swap(array,low,high)
			return high

def Swap(array,elementLeft,elementRight):
	tmp = array[elementLeft]
	array[elementLeft] = array[elementRight]
	array[elementRight] = tmp

def Partition(array,left,right):
	pivot = array[left]
	
	i = left + 1

	for j in range(left+1,right+1):
		if (array[j] < pivot):
			Swap(array,j,i)
			i = i + 1

	# send pivot to the correct position
	Swap(array,left,i-1)
	return (i-1)

filename = 'QuickSort.txt'
array = [line.rstrip('\n') for line in open(filename)]
array = [int(i) for i in array]

#array = [8,2,4,5,7,1]

numElements = len(array)
numComp = QuickSort(array,0,numElements-1,0)
print('Total number of comparisons',numComp)
