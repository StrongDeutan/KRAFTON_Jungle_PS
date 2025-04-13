#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    cin >> n;
    vector<vector<int>> rgb(n, vector<int>(3));
    vector<vector<int>> dp(n, vector<int>(3));
    for(int i = 0; i < n; i++){
        for(int k = 0; k < 3; k++){
            cin >> rgb[i][k];
        }
    }

    for(int i = 0; i < 3; i++){
        dp[0][i] = rgb[0][i];
    }

    for(int i = 1; i < n; i++){
        for(int k = 0; k < 3; k++){
            if(k == 0){
                dp[i][k] = min(dp[i-1][k+1] + rgb[i][k], dp[i-1][k+2] + rgb[i][k]);
            }
            else if(k == 1){
                dp[i][k] = min(dp[i-1][k-1] + rgb[i][k], dp[i-1][k+1] + rgb[i][k]);
            }
            else{
                dp[i][k] = min(dp[i-1][k-1] + rgb[i][k], dp[i-1][k-2] + rgb[i][k]);
            }
        }
    }

    int ans = 10000000;
    for(int i = 0; i < 3; i++){
        ans = min(ans, dp[n-1][i]);
    }

    cout << ans << "\n";
    return 0;
}