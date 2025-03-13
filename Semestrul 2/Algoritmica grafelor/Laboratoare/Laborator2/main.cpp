#include <iostream>
#include <fstream>
#include <queue>
#include <vector>

using namespace std;

ifstream fin("graf.txt");
int n;
bool adjacencyMatrix[100][100];
int distante[100];
bool vizatat[100];


void citire_adj() {
    fin >> n;
    int x, y;
    while (fin >> x >> y) {
        adjacencyMatrix[x][y] = true;
        adjacencyMatrix[y][x] = true;
    }
    fin.close();

  
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cout << adjacencyMatrix[i][j] << " ";
        }
        cout << endl;
    }
}


void BFS(int start) {
    queue<int> q;
    q.push(start);
    vizatat[start] = true;
    distante[start] = 0;

    while (!q.empty()) {
        int current = q.front();
        q.pop();

        
        cout << "Nod: " << current << ", len: " << distante[current] << endl;

       
        for (int i = 1; i <= n; i++) {
            if (adjacencyMatrix[current][i] && !vizatat[i]) {
                q.push(i);
                vizatat[i] = true;
                distante[i] = distante[current] + 1;
            }
        }
    }
}

int main() {
    citire_adj();

    int start;
    cout << "Introdu nod sursa: ";
    cin >> start;

   
    for (int i = 1; i <= n; i++) {
        distante[i] = -1;
        vizatat[i] = false;
    }

    BFS(start);

    return 0;
}