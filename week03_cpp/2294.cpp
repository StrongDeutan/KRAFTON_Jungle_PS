#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;
    vector<int> price(n);
    vector<int> dp(10001, -1);
    for (int i = 0; i < n; i++){
        int p;
        cin >> p;
        price[i] = p;
        dp[p] = 1;
    }

    for (int i = 1; i <= k; i++){
        int temp = INT_MAX;
        for(int j = 0; j < n; j++){
            if(i - price[j] < 1) continue;
            if(dp[i-price[j]] == -1) continue;
            temp = min(dp[i-price[j]], temp);
        }
        if(temp != INT_MAX){
            // cout << i << " i " << temp << " temp \n";
            if(dp[i] != -1){
                dp[i] = min(dp[i], temp + 1);
            }
            else{
                dp[i] = temp + 1;
            }
        }
    }

    cout << dp[k];


}