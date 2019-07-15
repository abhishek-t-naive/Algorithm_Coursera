//Implementation of Quick-Sort algorithm in Python as taught in the course: Design and Analysis of Algorithms on Coursera

#include <stdio.h>
#include <iostream>

using namespace std;

int ChooseMedian(int low, int middle, int high){
	if((low < middle && middle < high) || (high < middle && middle < low))
		return middle;
	else if((middle < low && low < high) || (high < low && low < middle))
		return low;
	else if((low < high && high < middle) || (middle < high && high < low))
		return high;	
}

int ChoosePivot(int *array, int low, int high, int flag){
	int middle;
	if (flag == 0)
		//choosing first element of array as pivot element
		return(array[low]);
	else if(flag == 1)
		//choosing last element of array as pivot element
		return(array[high]);
	else{
		if((high-low+1)%2 == 0)
			middle = (high-low+1)/2 - 1;
		else
			middle = (high-low+1)/2;
		return (ChooseMedian(array[low],array[middle],array[high]));
	}
}

void Swap(int *array,int elementLeft,int elementRight){
	int tmp = array[elementLeft];
	array[elementLeft] = array[elementRight];
	array[elementRight] = tmp;
}

int Partition(int *array, int left, int right, int flag){
	int pivot = ChoosePivot(array,left,right,flag);
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
		int numComparisons = 0;
		numComparisons = numComparisons + high - low;

		int pivotIndex = Partition(array, low, high, flag);
		
		QuickSort(array, low, pivotIndex-1, flag);
		QuickSort(array, pivotIndex+1, high, flag);

		return (numComparisons);
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
