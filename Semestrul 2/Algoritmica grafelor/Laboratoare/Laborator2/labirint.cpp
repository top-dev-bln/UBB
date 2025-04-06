#include <iostream>
#include <fstream>
#include <vector>
#include <queue>

using namespace std;

struct Position {
    int x, y;
};

vector<string> maze;
int n, m;
Position start, finish;
ifstream fin("labirint_2.txt");


void bfs() {
    vector<vector<bool> > visited(n, vector<bool>(m, false));
    vector<vector<Position> > parent(n, vector<Position>(m, Position()));

    if (parent.size() != n || parent[0].size() != m) {
        return;
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            parent[i][j].x = -1;
            parent[i][j].y = -1;
        }
    }

    queue<Position> q;

    q.push(start);
    visited[start.x][start.y] = true;

    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};

    while (!q.empty()) {
        Position current = q.front();
        q.pop();

        if (current.x == finish.x && current.y == finish.y) {
            break;
        }

        for (int i = 0; i < 4; i++) {
            int nx = current.x + dx[i];
            int ny = current.y + dy[i];
            if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny] && (maze[nx][ny] == ' ' || maze[nx][ny] == 'F')) {
                visited[nx][ny] = true;
                parent[nx][ny] = current;
                Position nextPos;
                nextPos.x = nx;
                nextPos.y = ny;
                q.push(nextPos);
            }
        }
    }


    Position cur = finish;
    while (!(cur.x == start.x && cur.y == start.y)) {
        if (cur.x < 0 || cur.x >= n || cur.y < 0 || cur.y >= m) {

            return;
        }

        Position prev = parent[cur.x][cur.y];
        if (prev.x == -1) {
            return;
        }
        if (maze[cur.x][cur.y] != 'F') {
            maze[cur.x][cur.y] = '*';
        }
        cur = prev;
    }
}

int main() {


    string line;
    while (getline(fin, line)) {
        maze.push_back(line);
    }
    fin.close();

    if (maze.empty()) {
        return 0;
    }

    n = maze.size();
    m = maze[0].size();


    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (maze[i][j] == 'S') {
                start.x = i;
                start.y = j;
            }
            if (maze[i][j] == 'F') {
                finish.x = i;
                finish.y = j;
            }
        }
    }

    bfs();


    for (int i = 0; i < maze.size(); i++) {
        cout << maze[i] << endl;
    }
    return 0;
}
