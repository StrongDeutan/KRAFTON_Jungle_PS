#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    cin >> n;
    vector<vector<int>> cost(n + 1, vector<int>(n + 1, 0));
    vector<vector<int>> dp(n + 1, vector<int>(n + 1, INT_MAX));
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            cin >> cost[i][j];
        }
    }

    




    return 0;
}