# Implementation of Quick-Sort algorithm in Python as taught in the course: Design and Analysis of Algorithms on Coursera

def QuickSort(array, low, high,flag):
	if(low<high):	
		numComparisons = 0
		numComparisons = numComparisons + high - low
		
		pivotIndex = Partition(array,low,high,flag)
		
		QuickSort(array,low,pivotIndex-1,flag)
		QuickSort(array,pivotIndex+1,high,flag)
		
		return numComparisons

def ChoosePivot(array,low,high,flag):
	if (flag == 0):
		#choosing first element of array as pivot element
		return(array[low])
	elif(flag == 1):
		#choosing last element of array as pivot element
		return(array[high])
	else:
		if((high-low+1)%2 == 0):
			middle = (high-low+1)//2 - 1
		else:
			middle = (high-low+1)//2
		middleElem = array[middle]
		return (ChooseMedian(array[low],array[middle],array[high]))

def ChooseMedian(low,middle,high):
	if((low < middle and middle < high) or (high < middle and middle < low)):
		return middle
	elif((middle < low and low < high) or (high < low and low < middle)):
		return low
	elif((low < high and high < middle) or (middle < high and high < low)):
		return high

def Swap(array,elementLeft,elementRight):
	tmp = array[elementLeft]
	array[elementLeft] = array[elementRight]
	array[elementRight] = tmp
	#return array

def Partition(array,left,right,flag):
	pivot = ChoosePivot(array,left,right,flag)
	i = left + 1
	
	for j in range(left+1,right+1):
		if (array[j] < pivot):
			Swap(array,j,i)
			i = i + 1

	# send pivot to the correct position
	Swap(array,left,i-1)
	return (i-1)

array = [7,5,15,6,1,4,12]
numElements = len(array)
numComp = QuickSort(array,0,numElements-1,2)
print('Total number of comparisons',numComp)
print(array)
