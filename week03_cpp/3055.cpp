#include <bits/stdc++.h>

using namespace std;

typedef tuple<int, int, int, int> tp;


int main(){
    int r, c;
    cin >> r >> c;
    vector<vector<char>> forest(r, vector<char>(c));
    

    int d_x, d_y;       // destination
    int s_x, s_y;        // start


    for (int i = 0; i < r; i++){
        for(int k = 0; k < c; k++){
            cin >> forest[i][k];
            if(forest[i][k] == 'D'){
                d_x = i;
                d_y = k;
            }
            if(forest[i][k] == 'S'){
                s_x = i;
                s_y = k;
            }
        }
    }

    priority_queue<tp, vector<tp>, greater<tp>> pq;

    for(int i = 0; i < r; i++){
        for(int k = 0; k < c; k++){
            if(forest[i][k] == '*'){
                tp p = make_tuple(0, 0, i, k);
                pq.push(p);
            }
        }
    }

    tp temp = make_tuple(0, 1, s_x, s_y);
    pq.push(temp);

    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};

    int ans = 0;

    while(!pq.empty()){
        auto cur = pq.top();
        pq.pop();

        int min = get<0>(cur);
        int type = get<1>(cur);
        int x = get<2>(cur);
        int y = get<3>(cur);



        if(type == 0){
            for (int i = 0; i < 4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                if(nx < 0 || ny < 0 || nx >= r || ny >= c) continue;
                if(forest[nx][ny] == 'D') continue;
                if(forest[nx][ny] == '*') continue;
                if(forest[nx][ny] == 'S') continue;
                if(forest[nx][ny] == 'X') continue;
                forest[nx][ny] = '*';
                pq.push(make_tuple(min + 1, type, nx, ny));
            }
        }
        else{
            if(x == d_x && y == d_y){
                ans = min;
                break;
            }

            for (int i = 0; i < 4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];

                if(nx < 0 || ny < 0 || nx >= r || ny >= c) continue;
                if(forest[nx][ny] == '*') continue;
                if(forest[nx][ny] == 'S') continue;
                if(forest[nx][ny] == 'X') continue;
                forest[nx][ny] = 'S';
                pq.push(make_tuple(min + 1, type, nx, ny));
            }

        }
    }

    if(ans == 0){
        cout << "KAKTUS";
    }
    else{
        cout << ans;
    }
    return 0;
}