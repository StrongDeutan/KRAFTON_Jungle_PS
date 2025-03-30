#include <bits/stdc++.h>
using namespace std;

typedef pair<int, pair<int, int>> P; 

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    
    vector<vector<int>> board(n, vector<int>(n));
    vector<vector<int>> dist(n, vector<int>(n, INT_MAX)); 

    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < n; j++) {
            board[i][j] = s[j] - '0'; 
        }
    }

    priority_queue<P, vector<P>, greater<P>> pq; 
    pq.push({0, {0, 0}});
    dist[0][0] = 0;

    int dx[4] = {1, 0, -1, 0};
    int dy[4] = {0, 1, 0, -1};

    while (!pq.empty()) {
        auto [cnt, pos] = pq.top();
        pq.pop();
        int x = pos.first, y = pos.second;

        if (x == n - 1 && y == n - 1) {
            cout << cnt; 
            return 0;
        }

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i], ny = y + dy[i];
            if (nx < 0 || ny < 0 || nx >= n || ny >= n) continue;

            int new_cnt = cnt + (board[nx][ny] == 0); 
            if (dist[nx][ny] > new_cnt) { 
                dist[nx][ny] = new_cnt;
                pq.push({new_cnt, {nx, ny}});
            }
        }
    }
}
