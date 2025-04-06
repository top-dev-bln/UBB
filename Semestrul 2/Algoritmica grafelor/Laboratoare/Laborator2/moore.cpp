//
// Created by Balan Andrei Daniel on 27.03.2025.
//
#include <iostream>
#include <fstream>
#include <queue>
#include <vector>


using namespace std;

ifstream fin("graf.txt");
int n;
bool adjacencyMatrix[100][100];
int distante[100];
bool vizitat[100];
int predecesor[100];

void moore(int start) {
    for (int i = 1; i <= n; i++) {
        distante[i] = -1;
        vizitat[i] = false;
        predecesor[i] = -1;
    }

    queue<int> q;
    q.push(start);
    distante[start] = 0;
    vizitat[start] = true;

    while (!q.empty()) {
        int current = q.front();
        q.pop();

        for (int i = 1; i <= n; i++) {
            if (adjacencyMatrix[current][i] && !vizitat[i]) {
                q.push(i);
                vizitat[i] = true;
                distante[i] = distante[current] + 1;
                predecesor[i] = current;
            }
        }
    }


    for (int i = 1; i <= n; i++) {
        if (distante[i] != -1) {
            cout << "Distanta minima de la nodul " << start << " la nodul " << i << " este: " << distante[i] << endl;
        } else {
            cout << "Nu exista drum de la nodul " << start << " la nodul " << i << endl;
        }
    }


}


int main() {
    fin >> n;
    int x, y;
    while (fin >> x >> y) {
        adjacencyMatrix[x][y] = true;
    }
    fin.close();

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cout << adjacencyMatrix[i][j] << " ";
        }
        cout << endl;
    }

    char opt;
    cout << endl << ">>> ";
    cin >> opt;

    if (opt == '1') {
        int start;
        cout << "Introdu nod sursa: ";
        cin >> start;

        moore(start);
    }

    return 0;
}