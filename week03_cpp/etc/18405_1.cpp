#include <iostream>
#include <tuple>
#include <queue>

using namespace std;
typedef tuple<int, int, int> tp;       // virus_num, x, y
int main(){
    int n, k;
    cin >> n >> k;

    vector<vector<int>> virus(n, vector<int>(n));
    
    priority_queue<tp, vector<tp>, greater<tp>> pq1;
    priority_queue<tp, vector<tp>, greater<tp>> pq2;

    for(int i = 0; i < n; i++){
        for(int p = 0; p < n; p++){
            cin >> virus[i][p];
            if(virus[i][p] != 0){
                tp temp = make_tuple(virus[i][p], i, p);
                pq1.push(temp);
            }
        }
    }


    int s, px, py;
    cin >> s >> px >> py;

    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};

    while(s--){
        if(pq2.empty()){
            while(!pq1.empty()){
                auto cur = pq1.top();
                int v_n = get<0>(cur);
                int x = get<1>(cur);
                int y = get<2>(cur);
                pq1.pop();
                for(int i = 0; i < 4; i++){
                    int nx = x + dx[i];
                    int ny = y + dy[i];
                    if(nx < 0 || ny < 0 || nx >= n || ny >= n) continue;
                    if(virus[nx][ny] != 0) continue;
                    virus[nx][ny] = v_n;
                    tp temp = make_tuple(v_n, nx, ny);
                    pq2.push(temp);
                }
            }

        }
        else{
            while(!pq2.empty()){
                auto cur = pq2.top();
                int v_n = get<0>(cur);
                int x = get<1>(cur);
                int y = get<2>(cur);
                pq2.pop();
                for(int i = 0; i < 4; i++){
                    int nx = x + dx[i];
                    int ny = y + dy[i];
                    if(nx < 0 || ny < 0 || nx >= n || ny >= n) continue;
                    if(virus[nx][ny] != 0) continue;
                    virus[nx][ny] = v_n;
                    tp temp = make_tuple(v_n, nx, ny);
                    pq1.push(temp);
                }
            }
        }

    }
    
    
    cout << virus[px - 1][py - 1];



    return 0;
}