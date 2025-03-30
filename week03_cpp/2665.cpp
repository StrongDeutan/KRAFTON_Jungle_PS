#include <bits/stdc++.h>

using namespace std;

typedef pair<int, pair<int, int>> P;



int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin  >> n;
    vector<vector<int>> board(n, vector<int>(n, 0));
    vector<vector<bool>> visit(n, vector<bool>(n, false));
    for (int i = 0; i < n; i++){
        string s;
        cin >> s;
        for (int k = 0; k < n; k++){
            if(s[k] == '1'){
                board[i][k] = 1;
            }
        }
    }
    priority_queue<P> pq;
    int black_count = 0; 

    int dx[4] = {1, 0, -1, 0};
    int dy[4] = {0, 1, 0, -1};

    pq.push(make_pair(board[0][0], make_pair(0, 0)));
    visit[0][0] = true;

    while(!pq.empty()){
        P cur = pq.top();
        pq.pop();
        int x = cur.second.first;
        int y = cur.second.second;

        if(cur.first == 0){
            black_count += 1;
        }
        if(x == n - 1 && y == n - 1){
            break;
        }

        for (int i = 0; i < 4; i++){
            if(x + dx[i] < 0 || x + dx[i] > n - 1 || y + dy[i] < 0 || y + dy[i] > n - 1){
                continue;
            }            
            else if(visit[x + dx[i]][y + dy[i]]){
                continue;
            }
            else{
                visit[x+ dx[i]][y + dy[i]] = true;
                pq.push(make_pair(board[x + dx[i]][y + dy[i]], make_pair(x + dx[i], y + dy[i])));
            }

        }


    }

    cout << black_count;
}