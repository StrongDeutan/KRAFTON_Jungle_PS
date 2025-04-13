#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> iput(n+1, 0);
    vector<int> dp(n+1, 0);
    for(int i = 1; i <= n; i++){
        cin >> iput[i];
    }
    dp[1] = iput[1];
    dp[2] = dp[1] + iput[2];

    for(int i = 3; i<= n; i++){
        dp[i] = max(dp[i-1], max(dp[i-2] + iput[i], dp[i-3] + iput[i-1] + iput[i]));
    }

    for(int i = 1; i <= n; i++){
        dp[n] = max(dp[n], dp[i]);
    }

    cout << dp[n] << "\n";



    return 0;
}