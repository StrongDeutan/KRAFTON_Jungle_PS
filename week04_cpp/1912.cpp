#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> read;
    while(n--){
        int k;
        cin >> k;
        read.push_back(k);
    }
    vector<int> dp(read.size(), 0);
    dp[0] = read[0];

    for(int i = 1; i < read.size(); i++){
        dp[i] = max(read[i], dp[i - 1] + read[i]);
    }
    int m = -100001;
    for(int i = 0; i < read.size(); i++){
        if(dp[i] > m) m = dp[i];
    }
    
    cout << m << "\n";

    return 0;
}