#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("adj.txt");
int adj[100][100];
int n;

int main() {
    fin >> n;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            fin >> adj[i][j];

            if (adj[i][j] == 1) {
                adj[j][i] = 1;
            }
        }
    }


    for (int k = 1; k <= n; k++) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                // aici e ca daca am de la i la k si dupa la j sa le schimb sa treaca direct de la i la j
                if (adj[i][k] == 1 && adj[k][j] == 1 && i!=j) {
                    adj[i][j] = 1;
                }
            }
        }
    }


    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cout << adj[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}