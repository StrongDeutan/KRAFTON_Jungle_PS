#include <bits/stdc++.h>

using namespace std;

// time limit

int main(){
    string a, b;
    cin >> a >> b;
    int col = a.size();
    vector<vector<int>> dp(2, vector<int>(col, 0));
    bool flag = true;                        //    true -> 0->1 false-> 1->0
    for(int i = 0; i < col; i++){
        if(b[0] == a[i]){
            dp[0][i] = 1;
        }
    }

    for(int i = 1; i < b.size(); i++){
        for(int j = 0; j< col; j++){
            if(b[i] == a[j]){
                if(flag){
                    dp[1][j] = dp[0][j-1] + 1;
                }
                else{
                    dp[0][j] = dp[1][j - 1] + 1;
                }
            }
            else{
                if(flag){
                    dp[0][j] = 0;
                }
                else{
                    dp[1][j] = 0;
                }
            }
        }
        flag = !flag;
    }

    int ans = 0;
    int idx = 0;
    int row;
    if(flag){
        row = 0;
    }
    else{
        row = 1;
    }
    for(int i = 0; i < col; i++){
        if(dp[row][i] > ans){
            ans = dp[row][i];
            idx = i;
        }
    }   

    stack<char> stk;
    for(int i = idx; i > 0; i--){
        stk.push(a[i]);
    }
    cout << ans << "\n";
    while(!stk.empty()){
        cout << stk.top();
        stk.pop();
    }

    return 0;
}