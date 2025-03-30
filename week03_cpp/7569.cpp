#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int m, n, h;
    cin >> m >> n >> h;

    vector<vector<vector<int>>> boxes(h);
    int total = m * n * h;
    int not_even = 0;
    int even = 0;
    for(int i = 0; i < h; i++){
        boxes[i] = vector<vector<int>>(n, vector<int>(m));
        for(int j = 0; j < n; j++){
            for(int k = 0; k < m; k++){
                cin>> boxes[i][j][k];
                if(boxes[i][j][k] == -1){
                    total -= 1;
                }
                else if(boxes[i][j][k] == 0){
                    not_even++;
                }
                else{
                    even++;
                }
            }
        }
    }

    int dz[6] = {1, -1, 0, 0, 0, 0};
    int dx[6] = {0, 0, 1, -1, 0, 0};
    int dy[6] = {0, 0, 0, 0, 1, -1};

    int days = 0;
    int temp = -1;              // 변하지 않았을 경우 세기

    while(even != total){
        if(temp == even){
            days = -1;
            break;
        }
        temp = even;

        queue<pair<int, pair<int, int>>> q;
        for(int i = 0; i < h; i++){
            for(int j = 0; j < n; j++){
                for(int k = 0; k < m; k++){
                    if(boxes[i][j][k] == -1 || boxes[i][j][k] == 0) continue;
                    for(int z = 0; z < 6; z++){
                        int nz = i + dz[z];
                        int nx = j + dx[z];
                        int ny = k + dy[z];
                        if(nz < 0 || nz >= h || nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                        if(boxes[nz][nx][ny] == 0){
                            q.push(make_pair(nz, make_pair(nx, ny)));
                        }
                    }
                }
            }
        }
        
        while(!q.empty()){
            auto cur = q.front();
            q.pop();
            if(boxes[cur.first][cur.second.first][cur.second.second] == 0){
                boxes[cur.first][cur.second.first][cur.second.second] = 1;
                even++;
                not_even--;
            }
        }

        days++;

    }

    cout << days;


    return 0;
}