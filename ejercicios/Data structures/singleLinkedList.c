#include <stdio.h>
#include <stdlib.h>

typedef struct Nodo{
	int dato;
	struct Nodo * siguiente;
}nodo;

typedef struct Lista{
	struct Nodo * cola;
	struct Nodo * inicio;
}lista;

void inicializar_lista(lista * ml){//es puntero porque quiero cambiar esa lista como tal... no hacer una copia de la lista 
	ml->inicio=malloc(sizeof(nodo));//ml es un puntero asi que va flecha y ya... sino sería punto :P
	ml->cola=ml->inicio;
	ml->inicio->siguiente=NULL;
	ml->inicio->dato=0;
}

void introducir_valor(int dat,lista *ml){
	nodo * Aux= malloc(sizeof(nodo));
	Aux->dato=dat;
	ml->cola->siguiente=Aux;
	ml->cola=Aux;
	ml->cola->siguiente=NULL;
}

void recorrer_inicio(lista *ml){
	nodo * Aux;
	Aux = ml->inicio->siguiente;
	printf("\n");
	while(Aux!=NULL){
		printf(" %d ",Aux->dato);
		Aux=Aux->siguiente;
	}
}

void recorrer_inverso(lista *ml){
	nodo * Aux;
	nodo * Aux2;
	Aux = ml->cola;
	Aux2 = ml->inicio;
	printf("\n");
	while(Aux!=ml->inicio){
		Aux2=ml->inicio;
		printf(" %d ",Aux->dato);
		while(Aux2->siguiente!=Aux){
			Aux2=Aux2->siguiente;
		}
		Aux=Aux2;
	}
}


int main(){
	lista Milista;						//lista * Milista = malloc(sizeof(lista));
	inicializar_lista(&Milista);		//inicializar_lista(Milista);
	introducir_valor(1,&Milista);
	introducir_valor(4,&Milista);
	introducir_valor(5,&Milista);
	introducir_valor(2,&Milista);
	introducir_valor(6,&Milista);
	recorrer_inicio(&Milista);
	recorrer_inverso(&Milista);
}
