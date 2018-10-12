#include <stdio.h>
#include <stdlib.h>

int main(){
	char cad[20]="holaholaholaholahola";
	int cad2[128]={0};
	for(int i=0 ; i<20 ; i++ ){
		cad2[ cad[i] ] =cad2[ cad[i] ]+1;
		printf("%c",cad[i]);
	}

	int maxi=0;
	int index=0;
	for(int i=0 ; i<128 ; i++){
		if(maxi < cad2[i]){
			maxi=cad2[i];
			index= i;
		}
	}


	printf("\n' %c '\n",index);



}


