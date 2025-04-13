#include <bits/stdc++.h>

using namespace std;

typedef unsigned short us;
#define short_max 65535


int main(){
    int n, m;
    cin >> n >> m;

    us col = (us)(sqrt(2*n) + 2);
    
    vector<vector<us>> dp(n+1, vector<us>(col + 1, short_max));
    // cout << col << ": col\n";
    // cout << "\n";
    //     for(int k = 0; k <= n; k++){
    //         for(int p = 0; p < col + 1; p++){
    //             cout << dp[k][p] << " ";
    //         }
    //         cout << "\n";
    //     }
    //     cout << "\n";

    vector<bool> visit(n + 1, true);
    while(m--){
        int p;
        cin >> p;
        visit[p] = false;
    }

    // for(int i = 0; i <= n; i++){
    //     cout << visit[i] << " ";
    // }
    // cout << "\n";

    dp[2][1] = 1;
    for(int i = 3; i <= n; i++){
        // cout << i << ": i\n";
        if(!visit[i]){
            // cout << "Skipping " << i << \n";
            continue;
        } 
        for(int j = 1; j < col; j++){
            if (i - j < 0 || j-1 < 0 || j+1 >= col+1) {
                continue;
            }
            dp[i][j] = min(min(dp[i-j][j-1], dp[i-j][j]), dp[i-j][j+1]);
            if(dp[i][j] != short_max) dp[i][j]++;
        }
        // cout << "\n";
        // for(int k = 0; k <= n; k++){
        //     cout << k << ": ";
        //     for(int p = 0; p < col + 1; p++){
        //         cout << dp[k][p] << " ";
        //     }
        //     cout << "\n";
        // }
        // cout << "\n";
    }
   
    
    us ans = short_max;

    if(visit[2] == false){
        cout << -1 << "\n";
        return 0;
    }

    if(visit[n] == true){
        for(int i = 0; i < col + 1; i++){
            ans = min(ans, dp[n][i]);
        }
    }
    
    if(ans != short_max){
        cout << ans << "\n";
    }
    else{
        cout << -1 << "\n";
    }
    return 0;
}