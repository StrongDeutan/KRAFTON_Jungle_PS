#include <bits/stdc++.h>

using namespace std;

int main(){
    int n, k;
    cin >> n >> k;
    vector<pair<int, int>> objs(n + 1);         // weight, value
    for(int i = 1; i <= n; i++){
        int w, v;
        cin >> w >> v;
        objs[i] = make_pair(w, v);
    }

    vector<vector<int>> dp(n + 1, vector<int>(k + 1, 0));
    for(int i = 1; i <= n; i++){
        for(int j = 0; j <= k; j++){
            if(j - objs[i].first >= 0){
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - objs[i].first] + objs[i].second);
            }
            else{
                dp[i][j] = dp[i-1][j];
            }
            
        }
    }

    cout << dp[n][k] << "\n";



    return 0;
}