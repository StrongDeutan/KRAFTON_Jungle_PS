#include<bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<vector<bool>> houses(n+2, vector<bool>(n+2, 0));
    for(int i = 1; i <= n; i++){
        string s;
        cin >> s;
        for(int j = 1; j <= n; j++){
            if(s[j -1] == '1'){
                houses[i][j] = 1;
            }
        }
    }

    priority_queue<int, vector<int>, greater<int>> pq;
    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, -1, 1};
    
    int count = 0;

    queue<pair<int, int>> q;
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            if(houses[i][j] == 1){
                count++;
                int temp = 0;
                houses[i][j] = 0;
                q.push(make_pair(i, j));
                while(!q.empty()){
                    auto cur = q.front();
                    temp++;
                    q.pop();
                    for(int k = 0; k < 4; k++){
                        if(houses[cur.first + dx[k]][cur.second + dy[k]] == 1){
                            q.push(make_pair(cur.first + dx[k],cur.second + dy[k]));
                            houses[cur.first + dx[k]][cur.second + dy[k]] = 0;
                        }
                    }                    
                }
                pq.push(temp);
            }

        }
    }
    cout << count << "\n";
    while(!pq.empty()){
        cout << pq.top() << "\n";
        pq.pop();
    }

    return 0;
}