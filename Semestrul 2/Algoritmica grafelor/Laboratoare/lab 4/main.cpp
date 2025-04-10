#include <iostream>
#include <fstream>
#include <vector>
#include <climits>


GraphData getGraphData(std::ifstream &input) {
    GraphData data;
    input >> data.nodes >> data.edges >> data.start;
    return data;
}

std::vector<GraphEdge> getEdges(std::ifstream &input, int edgeCount) {
    std::vector<GraphEdge> edgeList(edgeCount);
    for (int i = 0; i < edgeCount; ++i) {
        input >> edgeList[i].from >> edgeList[i].to >> edgeList[i].cost;
    }
    return edgeList;
}

void runBellmanFord(std::vector<int> &dist, const std::vector<GraphEdge> &edges, int nodeCount) {
    for (int i = 0; i < nodeCount - 1; ++i) {
        for (const auto &e : edges) {
            if (dist[e.from] != INT_MAX && dist[e.from] + e.cost < dist[e.to]) {
                dist[e.to] = dist[e.from] + e.cost;
            }
        }
    }
}



int main() {


    std::ifstream input("../2-in.txt");
    GraphData data = getGraphData(input);
    std::vector<GraphEdge> edges = getEdges(input, data.edges);

    std::vector<std::vector<std::pair<int, int>>> adjacency(data.nodes);
    std::vector<int> parent(data.nodes, -1);
    for (const auto &e : edges) {
        adjacency[e.from].push_back({e.to, e.cost});
    }

    std::vector<int> visited(data.nodes, 0);
    std::vector<int> dist(data.nodes, INT_MAX);
    dist[data.start] = 0;

    runDijkstra(data.start, data.nodes, dist, adjacency, visited, parent);

    for (int i = 0; i < data.nodes; ++i) {
        if (dist[i] == INT_MAX) {
            std::cout << i + 1 << ": INF" << std::endl;
        } else {
            std::cout << i + 1 << ": " << dist[i] << std::endl;
        }
    }

    return 0;
}