#include <bits/stdc++.h>

using namespace std;

int main(){
    int n, m;
    cin >> n >> m;
    vector<int> dp(n + 1, 0);
    for(int i = 0; i < m; i++){
        int k;
        cin >> k;
        dp[k] = -1;
    }

    dp[1] = 0;
    



    return 0;
}