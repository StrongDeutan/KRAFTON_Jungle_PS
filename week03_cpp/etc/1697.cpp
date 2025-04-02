#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;
    vector<int> dp(100001, -1);
    dp[n] = 0;
    queue<int> q;
    q.push(n);
    int count = 0;
    while(!q.empty()){
       
        int cur = q.front();
        q.pop();
        if(cur - 1 >= 0 && dp[cur - 1] == -1){
            dp[cur - 1] = dp[cur] + 1;
            if(cur-1 == k){
                break;
            }
            q.push(cur-1);
        }
        if(cur + 1 < 100001 && dp[cur+1] == -1){
            dp[cur+1] = dp[cur] + 1;
            if(cur+1 == k){
                break;
            }
            q.push(cur+1);
        }
        if(cur*2 < 100001 && dp[cur*2] == -1){
            dp[cur*2] = dp[cur] + 1;
            if(2*cur == k) break;
            q.push(2*cur);
        }

    }
    cout << dp[k];

    return 0;
}