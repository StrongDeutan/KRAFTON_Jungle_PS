#include <bits/stdc++.h>

using namespace std;

typedef tuple<int, int, int, int> tp;      // dist x y depth

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<vector<int>> maps(n, vector<int>(m, 0));
    vector<vector<int>> visit(n, vector<int>(m, false));
    for(int i = 0; i < n; i++){
        string s;
        cin >> s;
        for(int j = 0; j < m; j++){
            if(s[j] == '1') maps[i][j] = 1;
        }
    }

    bool check = false;
    priority_queue<tp, vector<tp>, greater<tp>> pq;
    pq.push(make_tuple(0, 0, 0, 1));
    visit[0][0] = true;
    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};

    int ans = 1;
    while(!pq.empty()){
        auto cur = pq.top();
        pq.pop();
        int cur_x = get<1>(cur);
        int cur_y = get<2>(cur);
        
        int di = get<0>(cur);
        int de = get<3>(cur);
        if(cur_x == n - 1 && cur_y == m - 1){
            ans = de;
            check = true;
            break;
        }

        for(int i = 0; i < 4; i++){
            int nx = cur_x + dx[i];
            int ny = cur_y + dy[i];

            if(nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
            if(maps[nx][ny] + di > 1) continue;
            if(visit[nx][ny]) continue;
            pq.push(make_tuple(maps[nx][ny] + di, nx, ny, de + 1));
            visit[nx][ny] = true;            
        }

    }
    if(check){
        cout << ans;
    }
    else{
        cout << -1;
    }
    







    return 0;
}