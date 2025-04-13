#include <bits/stdc++.h>

using namespace std;

#define mod 10007

int main(){
    int n;
    cin >> n;
    vector<int> dp(n + 1, 0);
    dp[1] = 1;
    dp[2] = 3;
    for(int i = 3; i <= n; i++){
        dp[i] = (dp[i-1] + (dp[i-2] * 2)) % mod;
    }
    cout << dp[n] << "\n";




    return 0;
}