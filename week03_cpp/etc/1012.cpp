#include <bits/stdc++.h>

using namespace std;



int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int m, n, k;
        cin >> m >> n >> k;
        vector<vector<bool>> land(n+2, vector<bool>(m+2, false));
        while(k--){
            int x, y;
            cin >> y >> x;
            land[x+1][y+1] = true;
        }

        int ans = 0;
        int dx[4] = {1, -1, 0, 0};
        int dy[4] = {0, 0, 1, -1};
        queue<pair<int, int>> q;
        for(int i = 1; i < n + 1; i++){
            for(int j = 1; j < m + 1; j++){
                if(land[i][j]){
                    ans++;
                    land[i][j] = false;
                    q.push(make_pair(i, j));
                    while(!q.empty()){
                        auto cur = q.front();
                        q.pop();
                        for(int k = 0; k < 4; k++){
                            int nx = cur.first + dx[k];
                            int ny = cur.second + dy[k];
                            if(land[nx][ny]){
                                land[nx][ny] = false;
                                q.push(make_pair(nx, ny));
                            }
                        }
                    }
                }
            }
        }
        cout << ans << "\n";
    }

    return 0;
}