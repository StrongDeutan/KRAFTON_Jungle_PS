#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> dp(n+1, INT_MAX);
    dp[3] = 1;
    dp[5] = 1;
    if(n == 3){
        cout << 1 << "\n";
    }
    else if(n == 5){
        cout << 1 << "\n";
    }
    else if(n >= 6){
        for(int i = 6; i <= n; i++){
            dp[i] = min(dp[i - 3], dp[i - 5]);
            if(dp[i] != INT_MAX){
                // cout << dp[i] << " " << i << "\n";
                dp[i]++;
            }
        }
        if(dp[n] == INT_MAX) cout << -1 << "\n";
        else cout << dp[n] << "\n";
    }
    else{
        cout << -1 << "\n";
    }






    return 0;
}