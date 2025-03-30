#include <bits/stdc++.h>

using namespace std;

typedef tuple<int, int, int, int> tp;        // days, z, x, y

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int m, n, h;
    cin >> m >> n >> h;

    vector<vector<vector<int>>> boxes(h);
    int total = m * n * h;
    
    int even = 0;
    for(int i = 0; i < h; i++){
        boxes[i] = vector<vector<int>>(n, vector<int>(m));
        for(int j = 0; j < n; j++){
            for(int k = 0; k < m; k++){
                cin>> boxes[i][j][k];
                if(boxes[i][j][k] == -1){
                    total -= 1;
                }
                else if(boxes[i][j][k] == 1){
                    even++;
                }
            }
        }
    }

    if(even == total){        //  이미 다 익음
        cout << 0;
        return 0;
    }

    int dz[6] = {1, -1, 0, 0, 0, 0};
    int dx[6] = {0, 0, 1, -1, 0, 0};
    int dy[6] = {0, 0, 0, 0, 1, -1};

    int days = 0;
    
    priority_queue<tp, vector<tp>, greater<tp>> pq;
    for(int i = 0; i < h; i++){
        for(int j = 0; j < n; j++){
            for(int k = 0; k < m; k++){
                if(boxes[i][j][k] == 1){
                    pq.push(make_tuple(0, i, j, k));
                }
            }
        }
    } 

    while(!pq.empty()){
        tp cur = pq.top();
        pq.pop();
        int d = get<0>(cur);
        int z = get<1>(cur);
        int x = get<2>(cur);
        int y = get<3>(cur);

        days = max(d, days);
        
        for(int i = 0; i < 6; i++){
            int nz = z + dz[i];
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(nz < 0 || nz >= h || nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if(boxes[nz][nx][ny] == 0){
                boxes[nz][nx][ny] = 1;
                even++;
                pq.push(make_tuple(d + 1, nz, nx, ny));
            }
        }

    }   

    if(total == even) cout << days;
    else cout << -1;

    return 0;
}