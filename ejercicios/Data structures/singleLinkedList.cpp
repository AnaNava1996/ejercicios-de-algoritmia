#include <iostream>
#include <string>
using namespace std;

class Perritos{
	public:
		int edad;
		string nombre;
		
		void print_nombre(){
			cout<<"el nombre es: "<<nombre<<"\n";
		}
};


int main(){
	Perritos Pepe;
	Pepe.nombre= "Pepe";
	
	Pepe.print_nombre();
}


