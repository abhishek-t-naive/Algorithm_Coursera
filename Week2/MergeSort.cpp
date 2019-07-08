//Implementation of merge sort algorithm in C++

#include <stdio.h>
#include <math.h>
#include <iostream>

using namespace std;

void Merge(int *data, int low, int mid, int high){
	int i = low;
	int j = mid+1;
	int k = 0;

	int sortedArray[high-low+1];

	for(k = 0; k < high-low+1; k++){
		if(i <= mid && j <= high){
			if(data[i] < data[j]){
				sortedArray[k] = data[i];
				i				= i + 1;
			}
			else{
				sortedArray[k] = data[j];
				j       = j+1;
			}
		}
		else if(i <= mid){
			sortedArray[k] = data[i];
			i				= i + 1;
		}
		else{
			sortedArray[k] = data[j];
			j       = j+1;
		}
	}

	for(i = low; i <= high; i++){
		data[i] = sortedArray[i-low];
	}	

}

void MergeSort(int *data, int low, int high){
	
	if (low < high){
		int middle = (low+high)/2;
		MergeSort(data,low,middle);
		MergeSort(data,middle+1,high);
		Merge(data,low,middle,high);
	}
}

int main(){
	
	//int data[16] = ['1', '3', '5', '7', '4', '6', '8', '2', '19', '15', '12', '11', '16', '17', '10', '20'];

	int numElements;
	
	cout <<"Enter the number of elements to be sorted: \n";
	cin >> numElements;

	int data[numElements];

	for(int i = 0; i < numElements; i++){
		cout << "Enter element " << i << ":\n";
		cin >> data[i];
	}

	MergeSort(data,0,numElements-1);

	cout <<"Sorted Data!\n";

	for(int i = 0 ; i < numElements; i++){
		cout <<"->"<<data[i];
	}

	return 0;	

}
