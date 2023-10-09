#include <bits/stdc++.h>
using namespace std;

vector<int> bellman(int src) {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> graph(m, vector<int>(3));
    
    for (int i = 0; i < m; i++) {
        cin >> graph[i][0] >> graph[i][1] >> graph[i][2];
    }
    vector<int> dist(n, INT_MAX);
    dist[src-1] = 0;
    for (int i = 0; i < n-1; i++) {
        for (auto edge : graph) {
            int u = edge[0], v = edge[1], w = edge[2];
            if (dist[u-1] != INT_MAX && dist[u-1] + w < dist[v-1]) {
                dist[v-1] = dist[u-1] + w;
            }
        }
    }
    vector<int> result(n);
    for (int i = 0; i < n; i++) {
        if (dist[i] == INT_MAX) {
            result[i] = 30000;
        } else {
            result[i] = dist[i];
        }
    }

    return result;
}

int main() {
    vector<int> result = bellman(1);
    for (auto num : result) {
        cout << num << " ";
    }
    return 0;
}