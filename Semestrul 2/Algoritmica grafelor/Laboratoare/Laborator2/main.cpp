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
}

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

void DFS_VISIT(int u) {
    vizitat[u] = true;
    cout << u << " ";

    for (int v = 1; v <= n; v++) {
        if (adjacencyMatrix[u][v] && !vizitat[v]) {
            DFS_VISIT(v);
        }
    }
}

void DFS() {

    for (int i = 1; i <= n; i++) {
        vizitat[i] = false;
    }

    cout << "Padurea descoperita de DFS:\n";
    for (int i = 1; i <= n; i++) {
        if (!vizitat[i]) {
            cout << "Componenta noua: ";
            DFS_VISIT(i);
            cout << endl;
        }
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



    char opt ;
    cout << endl <<">>>";
    cin >> opt;


    if (opt == '1') {
        int start;
        cout << "Introdu nod sursa: ";
        cin >> start;


        for (int i = 1; i <= n; i++) {
            distante[i] = -1;
            vizatat[i] = false;
        }

        BFS(start);

    }
    if(opt == '2') {
        DFS();

    }
    if(opt == '3') {
        //cerinta 3
    }
    if(opt == '4') {
        //cerinta 4
    }
    if(opt == '5') {
        //cerinta 5
    }



    return 0;
}


