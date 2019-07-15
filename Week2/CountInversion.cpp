//Implementation of merge sort algorithm in C++

#include <stdio.h>
#include <math.h>
#include <iostream>

using namespace std;

int Count_Split_Inv(int *data, int low, int mid, int high){
	int i = low;
	int j = mid+1;
	int k = 0;
	int invSplit = 0;

	int sortedArray[high-low+1];

	for(k = 0; k < high-low+1; k++){
		if(i <= mid && j <= high){
			if(data[i] < data[j]){
				sortedArray[k] = data[i];
				i				= i + 1;
			}
			else{
				sortedArray[k] = data[j];
				invSplit = invSplit + mid-low + 1 - i;
				//cout << "invSplit is: " << invSplit << "\n";
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
	return invSplit;
}

int Sort_and_Count(int *data, int low, int high){

	int middle;	
	int invLeft  = 0;
	int invRight = 0;
	int invSplit = 0;
	if (low < high){
		middle = (low+high)/2;
		invLeft		= Sort_and_Count(data,low,middle);
		invRight	= Sort_and_Count(data,middle+1,high);
		invSplit	= Count_Split_Inv(data,low,middle,high);
	}
	//int totInv = invLeft+invRight+invSplit;
	//cout << "Total inversions: " << totInv << "\n";
	return (invLeft+invRight+invSplit);
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

	int inversions = Sort_and_Count(data,0,numElements-1);

	cout << "Total inversions are: " << inversions << "\n";
	//cout <<"Sorted Data!\n";

	//for(int i = 0 ; i < numElements; i++){
	//	cout <<"->"<<data[i];
	//}

	return 0;	

}
