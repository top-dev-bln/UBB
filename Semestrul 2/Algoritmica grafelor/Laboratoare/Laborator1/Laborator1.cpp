#include <fstream>
#include <vector>
#include <iostream>

using namespace std;

ifstream fin("graph.txt");

int n;
int muchie;
bool adjacencyMatrix[100][100];
bool incidenceMatrix[100][500];
vector<int> neighbours[100];

void clearAdjacencyMatrix() {
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            adjacencyMatrix[i][j] = 0;
}

void clearIncidenceMatrix() {
    for (int i = 1; i <= n; i++)
        for (int j = 0; j < muchie; j++)
            incidenceMatrix[i][j] = 0;
    muchie = 0;
}

void clearNeighbours() {
    for (int i = 1; i <= n; i++)
        neighbours[i].clear();
}

void readAdiacenta() {
    fin >> n;
    int x, y;
    while (fin >> x >> y) {
        adjacencyMatrix[x][y] = true;
        adjacencyMatrix[y][x] = true;
    }
    fin.close();

    cout << "Matrice adiacenta:\n";
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cout << adjacencyMatrix[i][j] << " ";
        }
        cout << '\n';
    }
}

void Adiacenta2lista() {
    clearNeighbours();
    for (int i = 1; i <= n; i++) {
        for (int j = i + 1; j <= n; j++) {
            if (adjacencyMatrix[i][j]) {
                neighbours[i].push_back(j);
                neighbours[j].push_back(i);
            }
        }
    }
    clearAdjacencyMatrix();

    cout << "Lista adiacenta dupa conversie:\n";
    for (int i = 1; i <= n; i++) {
        cout << i << ": ";
        for (int j = 0; j < neighbours[i].size(); j++) {
            cout << neighbours[i][j] << " ";
        }
        cout << '\n';
    }
}

void Lista2Incidenta() {
    clearIncidenceMatrix();
    muchie = 0;
    for (int i = 1; i <= n; i++) {
        for (int v : neighbours[i]) {
            if (i < v) {
                incidenceMatrix[i][muchie] = 1;
                incidenceMatrix[v][muchie] = 1;
                muchie++;
            }
        }
    }
    clearNeighbours();

    cout << "Matrice incidenta dupa conversie:\n";
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < muchie; j++) {
            cout << incidenceMatrix[i][j] << " ";
        }
        cout << '\n';
    }
}

void Incidenta2Lista() {
    clearNeighbours();
    for (int j = 0; j < muchie; j++) {
        int u = -1, v = -1;
        for (int i = 1; i <= n; i++) {
            if (incidenceMatrix[i][j]) {
                if (u == -1) u = i;
                else {
                    v = i;
                    break;
                }
            }
        }
        if (u != -1 && v != -1) {
            neighbours[u].push_back(v);
            neighbours[v].push_back(u);
        }
    }
    clearIncidenceMatrix();

    cout << "Lista adiacenta dupa conversie:\n";
    for (int i = 1; i <= n; i++) {
        cout << i << ": ";
        for (int j = 0; j < neighbours[i].size(); j++) {
            cout << neighbours[i][j] << " ";
        }
        cout << '\n';
    }
}

void Lista2Adiancenta() {
    clearAdjacencyMatrix();
    for (int i = 1; i <= n; i++) {
        for (int v : neighbours[i]) {
            adjacencyMatrix[i][v] = 1;
            adjacencyMatrix[v][i] = 1;
        }
    }
    clearNeighbours();

    cout << "Matrice adiacenta dupa conversie:\n";
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cout << adjacencyMatrix[i][j] << " ";
        }
        cout << '\n';
    }
}


int main() {
    readAdiacenta();

    Adiacenta2lista();
    Lista2Incidenta();
    Incidenta2Lista();
    Lista2Adiancenta();
    Adiacenta2lista();

    return 0;
}
