#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> dp(n + 1, 0);
    vector<int> stairs(n + 1, 0);
    for(int i = 1; i <= n; i++){
        cin >> stairs[i];
    }
    dp[0] = 0;
    dp[1] = stairs[1];
    dp[2] = dp[1] + stairs[2];
    
    for(int i = 3; i <= n; i++){
        dp[i] = max(dp[i-2] + stairs[i], stairs[i-1] + dp[i-3] + stairs[i]);
    }

    cout << dp[n];

    return 0;
}