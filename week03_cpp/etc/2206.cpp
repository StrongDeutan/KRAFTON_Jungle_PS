#include <bits/stdc++.h>
using namespace std;

typedef tuple<int, int, int, int> tp;          // weight, row, col, depth

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<vector<int>> board(n, vector<int>(m, 0));
    vector<vector<int>> dist(n, vector<int>(m, INT_MAX));
    vector<vector<int>> status(n, vector<int>(m, 0));
    for(int i = 0; i < n; i++){
        string s;
        cin >> s;
        for(int j = 0; j < m; j++){
            if(s[j] == '1') board[i][j] = 1;
        }
    }

    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};

    priority_queue<tp, vector<tp>, greater<tp>> pq;
    
    int ans = 1;
    dist[0][0] = 0;
    status[0][0] = 2;

    for(int i = 0; i < 4; i++){
        int nx = dx[i];
        int ny = dy[i];
        if(nx < 0 || ny < 0 || nx >= n || ny >= m){
            continue;
        }
        dist[nx][ny] = board[nx][ny];
        status[nx][ny] = 1;
        pq.push(make_tuple(dist[nx][ny], nx, ny, 2));
    }
    while(!pq.empty()){
        auto cur = pq.top();
        pq.pop();
        int cur_x = get<1>(cur);
        int cur_y = get<2>(cur);
        int d = get<0>(cur);
        if(status[cur_x][cur_y] == 2) continue;
        if(dist[cur_x][cur_y] < d) continue;
        status[cur_x][cur_y] = 2;

        if(cur_x == n - 1 && cur_y == m - 1) {ans = get<3>(cur); break;}
        for(int i = 0; i < 4; i++){
            int nx = cur_x + dx[i];
            int ny = cur_y + dy[i];
            if(nx < 0 || ny < 0 || nx >= n || ny >= m){
                continue;
            }
            if(status[nx][ny] == 2) continue;
            if(status[nx][ny] == 1){
                if(dist[nx][ny] >= d + board[nx][ny]){
                    dist[nx][ny] = d + board[nx][ny];
                    pq.push(make_tuple(d + board[nx][ny], nx, ny, get<3>(cur) + 1));
                }
            }
            else{
                status[nx][ny] = 1;
                dist[nx][ny] = d + board[nx][ny];
                pq.push(make_tuple(d + board[nx][ny], nx, ny, get<3>(cur) + 1));
            }
        }
    }

    if(dist[n-1][m-1] > 1) cout << -1;
    else{
        cout << ans;
    }


    return 0;
}