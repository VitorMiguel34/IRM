#include <iostream>
#include <string>

using namespace std;

class Pessoa{
    private:
        string nome;
        int idade;
    public:
        Pessoa(string n, int i){
            nome = n;
            idade = i;
            cout << "Construindo o objeto..." << endl;
        }

        ~Pessoa(){
            cout << nome << " foi apagado da memória!" << endl;
        }

        void apresentar(){
            cout << "Meu nome é " << nome << " e eu tenho " << idade << " anos" << endl;
        }
};

int main(){
    // Objeto na stack
    Pessoa p("Victor",16);
    p.apresentar();

    // Objeto na heap
    Pessoa* p2 = new Pessoa("Joao",16);
    p2->apresentar();

    delete p2;
    return 0;
}