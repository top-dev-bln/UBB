#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <fstream>

using namespace std;

ifstream fin("1-in.txt");

struct Edge {
    int to, weight;
};

void dijkstra(int start, int end, const vector<vector<Edge>>& graph) {
    int n = graph.size();
    vector<int> dist(n, INT_MAX);
    vector<int> parent(n, -1);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;

    dist[start] = 0;
    pq.push({0, start});

    while (!pq.empty()) {
        int d = pq.top().first;
        int u = pq.top().second;
        pq.pop();

        if (d > dist[u]) continue;

        for (const auto& edge : graph[u]) {
            int v = edge.to;
            int weight = edge.weight;

            if (dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                parent[v] = u;
                pq.push({dist[v], v});
            }
        }
    }

    if (dist[end] == INT_MAX) {
        cout << "Nu exista drum de la " << start << " la " << end << ".\n";
        return;
    }

    cout << "Drumul minim de la " << start << " la " << end << " este " << dist[end] << ".\n";

}

int main() {
    int n, u, v, w;
    fin >> n;

    vector<vector<Edge>> graph(n);

    while (fin >> u >> v >> w) { 
        graph[u].push_back({v, w});
    }

    int start, end;
    cout << "Introduceti nodul de start si nodul de final: ";
    cin >> start >> end;

    dijkstra(start, end, graph);

    return 0;
}