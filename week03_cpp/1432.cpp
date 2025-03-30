#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    int cur_idx = n;
    vector<vector<char>> g(n+1, vector<char>(n+1,0));
    vector<int> result(n+1, 0);
    priority_queue<int> pq;
    vector<int> in_degree(n + 1); // 입력을 transpose 실제로는 out

    for(int i = 1; i <= n; i++){
        string s;
        cin >> s;
        for(int j = 1; j <= n; j++){
            g[j][i] = s[j - 1];
            if(g[j][i] == '1') in_degree[i]++;
        }
    }

    for(int i = 1; i <= n; i++){
        if(in_degree[i] == 0){
            pq.push(i);
        }
    }

    bool check = true;

    if(pq.empty()){
        check = false;
    }
    while(!pq.empty()){
        int idx = pq.top();
        pq.pop();
        if(result[idx] != 0){
            check = false;
            break;
        }
        result[idx] = cur_idx;
        cur_idx--;
        for(int i = 1; i <= n; i++){
            if(g[idx][i] == '1'){
                in_degree[i]--;
                if(in_degree[i] == 0){
                    pq.push(i);
                }
            }
        }
    }

    if(check){
        for(int i = 1; i <= n; i++){
            cout << result[i] << " ";
        }
    }
    else{
        cout << -1;
    }
    
}