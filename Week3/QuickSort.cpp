//Implementation of Quick-Sort algorithm in Python as taught in the course: Design and Analysis of Algorithms on Coursera

#include <stdio.h>
#include <iostream>

using namespace std;

void Swap(int *array,int elementLeft,int elementRight){
	int tmp = array[elementLeft];
	array[elementLeft] = array[elementRight];
	array[elementRight] = tmp;
}

void ChooseMedian(int *array, int low, int middle, int high){
	if((array[low] <= array[middle] && array[middle] <= array[high]) || (array[high] <= array[middle] && array[middle] <= array[low]))
		Swap(array,low,middle);
	else if((array[low] <= array[high] && array[high] <= array[middle]) || (array[middle] <= array[high] && array[high] <= array[low]))
		Swap(array,low,high);	
}

void ChoosePivot(int *array, int low, int high, int flag){
	int middleIndex,middle;
	if (flag == 0)
		//choosing first element of array as pivot element
		Swap(array,low,low);
	else if(flag == 1)
		//choosing last element of array as pivot element
		Swap(array,low,high);
	else{
		//choosing median element of array as pivot element
		if((high-low+1)%2 == 0)
			middleIndex = (high-low+1)/2 - 1;
		else
			middleIndex = (high-low+1)/2;
		middle = low + middleIndex;
		ChooseMedian(array,low,middle,high);
	}
}

int Partition(int *array, int left, int right){
	int pivot = array[left];
	int i = left + 1;
	
	for(int j = left+1;j <= right;j++){
		if(array[j] < pivot){
			Swap(array,j,i);
			i = i + 1;
		}
	}
	
	Swap(array, left, i-1);
	return (i-1);
}

int QuickSort(int *array, int low, int high, int flag){
	if(low < high){
		
		int length = high - low;
		
		ChoosePivot(array,low,high,flag);

		int pivotIndex = Partition(array, low, high);
		
		int leftComparisons  = QuickSort(array, low, pivotIndex-1, flag);
		int rightComparisons = QuickSort(array, pivotIndex+1, high, flag);

		return (leftComparisons+rightComparisons+length-1);
	}
}

int main(){
	int numElements;

	cout << "Enter the number of elements you want to sort: \n";
	cin >> numElements;

	int data[numElements];
	
	for(int i = 0; i < numElements; i++){
		cout << "Enter element " << i << ":\n";
		cin >> data[i];
	}

	int numComp = QuickSort(data, 0, numElements-1,0);
	
	cout <<"Sorted Data!\n";

	for(int i = 0 ; i < numElements; i++){
		cout <<"->"<<data[i];
	}

	return 0;	
}
