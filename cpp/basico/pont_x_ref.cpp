#include <iostream> 

using namespace std;

void trocarComPonteiro(int* a, int* b){
    int c = *a; // 'c' guarda o valor do endereço para onde 'a' aponta
    *a = *b; // o valor do endereço onde 'a' aponta passa a ser o valor do endereço que 'b' aponta
    *b = c; // o valor do endereço para onde b aponta passa a ser o valor de 'c'(antigo valor do endereço que 'a' apontava)
}

void trocarComReferencia(int& a, int& b){
    int c = a; // 'c' quarda o valor da referência
    a = b; // o valor de 'a' passa a ser o de 'b'
    b = c; // o valor de 'b' passar a ser o de 'c'
    cout << "oi" << endl;
}

int main(){
    int x = 10;
    int y = 2;
    int* p1 = &x;
    int* p2 = &y;
    int &r1 = x;
    int &r2 = y;
    cout << "x: " << x << " y: " << y << endl;
    cout << "Invertendo variáveis com ponteiros..." << endl;
    trocarComPonteiro(p1, p2);
    cout << "x: " << x << " y: " << y << endl;
    cout << "Invertendo variáveis com referências..." << endl;
    trocarComReferencia(r1,r2);
    cout << "x: " << x << " y: " << y << endl;
    return 0;
}