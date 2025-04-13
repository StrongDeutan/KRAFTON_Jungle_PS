#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long ll;

int main(){
    int n;
    cin >> n;
    vector<vector<ll>> board(n, vector<ll>(n));
    vector<vector<ll>> dp(n, vector<ll>(n, 0));
    
    for(int i = 0; i < n; i++){
        for(int k = 0; k < n; k++){
            cin >> board[i][k];
        }
    }
    
    dp[0][0] = 1; 
    
    for(int i = 0; i < n; i++){
        for(int k = 0; k < n; k++){
            if(dp[i][k] == 0 || board[i][k] == 0) continue;
            
            int d_move = board[i][k];
            if(i + d_move < n){
                dp[i + d_move][k] += dp[i][k];
            }
            if(k + d_move < n){
                dp[i][k + d_move] += dp[i][k];
            }
        }
    }
    
    cout << dp[n-1][n-1] << "\n";
    return 0;
}
