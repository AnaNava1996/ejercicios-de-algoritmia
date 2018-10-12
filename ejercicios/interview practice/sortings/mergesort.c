#include <stdio.h>
#include <stdlib.h>

void mergesort(int *array, int len){
	if(len==1){
		array=array;
	}
	else if(len==2){
		
	}
	int half=len/2;
	int arre1[half];
	for(int i=0; i<half ; i++){
		arre1[i]=array[i];
	}
	int arre2[len-half];
	for(int i=half; i<(len-half) ; i++){
		arre1[i]=array[i];
	}
	mergesort(arre1);
	mergesort(arre2);
		
}

int main(){
	int array[9]={1,6,9,2,5,3,7,8,4};
	mergesort(array,9);	
	

}
