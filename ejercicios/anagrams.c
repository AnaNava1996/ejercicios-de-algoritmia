#include <stdio.h>
#include <stdlib.h>


void mergesort(char * cad){
	

}

int main(int argc, char ** argv){
	int len1=0;
	int len2=0;
	while(argv[1][len1]!='\0'){
		len1++;
	}
	while(argv[2][len2]!='\0'){
		len2++;
	}
	char * cad1=malloc((sizeof(char)*len1)+1);
	for(int i=0;i<len1 ; i++){
		cad1[i]=argv[1][i];
	}
	cad1[len1]='\0';
	char * cad2=malloc((sizeof(char)*len2)+1);	
	for(int i=0;i<len2 ; i++){
		cad2[i]=argv[2][i];
	}
	cad2[len2]='\0';
	printf("\n%s     %s\n",cad1,cad2);
	
	if(len1!=len2){
		printf("\nNot anagrams");
	}
	else{
		mergesort(cad1);
		mergesort(cad2);
	}
}












