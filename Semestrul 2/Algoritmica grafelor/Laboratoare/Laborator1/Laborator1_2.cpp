#include <fstream>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

ifstream fin("graph.txt");



int main() {
    int n;
    bool adjacencyMatrix[100][100] = { false };

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

    char opt;
    cout << "a. Determinati nodurile izolate" << endl;
    cout << "b. Determinati daca graful este regular" << endl;
    cout << "c. Determinati matricea distantelor" << endl;
    cout << "d. Determinati daca graful este conex" << endl;
    cout << "Introduceti optiunea: ";
    cout << endl;
    cout << " >>> ";
    cin >> opt;
    cout << endl;

    if (opt == 'a') {
        cout << "Nodurile izolate: ";
        bool izolat;
        for (int i = 1; i <= n; i++) {
            izolat = true;
            for (int j = 1; j <= n; j++) {
                if (adjacencyMatrix[i][j] == 1) {
                    izolat = false;
                    break;
                }
            }
            if (izolat) {
                cout << i << " ";
            }
        }
        cout << endl;
    }

    else if (opt == 'b') {
        cout << "Verificam daca graful este regular..." << endl;
        int grad_prim = -1;
        bool regular = true;

        for (int i = 1; i <= n; i++) {
            int grad_curent = 0;
            for (int j = 1; j <= n; j++) {
                if (adjacencyMatrix[i][j] == 1) grad_curent++;
            }
            if (grad_prim == -1) grad_prim = grad_curent;
            if (grad_curent != grad_prim) {
                regular = false;
                break;
            }
        }

        if (regular)
            cout << "Graful este regular" << endl;
        else
            cout << "Graful NU este regular" << endl;
    }

    else if (opt == 'c') {
        cout << "Matricea distantelor minime:\n";

        int dist[100][100];

        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                if (i == j) {
                    dist[i][j] = 0;
                }
                else {
                    dist[i][j] = -1;
                }

        for (int i = 1; i <= n; i++) {
            queue<int> q;
            q.push(i);

            while (!q.empty()) {
                int nod = q.front();
                q.pop();

                for (int a = 1; a <= n; a++) {
                    if (adjacencyMatrix[nod][a] == 1 && dist[i][a] == -1) {
                        dist[i][a] = dist[i][nod] + 1;
                        q.push(a);
                    }
                }
            }
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (dist[i][j] == -1)
                    cout << "- ";
                else
                    cout << dist[i][j] << " ";
            }
            cout << endl;
        }
    }

    else if (opt == 'd') {

        cout << "Verificam daca graful este conex..." << endl;
        queue<int> q;
        bool parcurse[100];

        for (int i = 1; i <= n; i++) {
            parcurse[i] = 0;
        }

        q.push(1);

        while (!q.empty()) {
            int nod = q.front();
            q.pop();

            for (int a = 1; a <= n; a++) {
                if (adjacencyMatrix[nod][a] == 1 && parcurse[a]==0) {
                    parcurse[a] = 1;
                    q.push(a);
                }
            }
        }

        bool conex = true;
    for (int i = 1; i <= n; i++) {
        if (parcurse[i] == 0) {
            conex = false;
            break;
        }

        

    }
    cout << conex;


    }

    return 0;
}
