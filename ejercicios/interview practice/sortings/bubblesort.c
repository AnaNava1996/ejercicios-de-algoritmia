#include <stdio.h>
#include <stdlib.h>

int main(int argc,char *argv[]){
	int temp;
	int array[argc-1];
	//printf("%d",argc);
	printf("\nUnsortered array:\n");
	char letra;
	for(int i=1 ; i<argc ; i++){
		letra=*argv[i];
		array[i-1]=letra-'0';
		printf("%d  ",array[i-1]);
	}
	printf("\nSortered array:");
	for(int i=(argc-2); i>0; i--){
		for (int j=0; j<i ; j++ ){
			if(array[j]>array[j+1]){
				temp=array[j+1];
				array[j+1]=array[j];
				array[j]=temp;			
			}
		}
	}
	printf("\n");
	for(int i=0; i<argc-1 ; i++){
		printf("%d  ", array[i]);
	}
}

