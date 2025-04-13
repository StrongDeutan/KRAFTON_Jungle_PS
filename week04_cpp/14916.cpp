#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> dp(n+1, INT_MAX);
    dp[2] = 1;
    dp[5] = 1;
    dp[4] = 2;
    for(int i = 6; i <= n; i++){
        dp[i] = min(dp[i-2], dp[i-5]);
        if(dp[i] != INT_MAX){
            dp[i] += 1;
        }
    }

    if(dp[n] == INT_MAX){
        cout << -1 << "\n";
    }
    else{
        cout << dp[n] << "\n";
    }



    return 0;
}