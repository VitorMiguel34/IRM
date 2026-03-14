#include <iostream>

using namespace std;

int main(){
    int n;
    cout << "Quantidade de numeros no array: ";
    cin >> n;
    int* numeros = new int[n];
    int numero;
    for(int i = 0; i < n; i++){
        cout << "Numero: ";
        cin >> numero;
        *(numeros+i) = numero; // ou "items[i] = item"
    }
    for(int i = 0; i < n; i++){
        cout << numeros[i] << endl;
    }
    delete[] numeros;
    return 0;
}