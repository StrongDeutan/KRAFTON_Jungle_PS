#include <bits/stdc++.h>

using namespace std;


int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<vector<int>> arr(n + 1, vector<int>(n+1, INT_MAX));
    int i, j;
    while(m--){
        cin >> i >> j;
        arr[i][j] = 1;
    }

    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            for(int k = 1; k <= n; k++){
                if(j == k){
                    arr[j][k] = 0;
                    continue;
                }
                if(arr[j][i] != INT_MAX and arr[i][k] != INT_MAX){
                    arr[j][k] = min(arr[j][k], arr[j][i] + arr[i][k]);
                }
            }
        }
    }

    // for (int i = 1; i <= n; i++){
    //     for(int j = 1; j <= n; j++){
    //         cout << arr[i][j] << " ";
    //     }
    //     cout << "\n";
    // }
    
    int ans = 0;
    int count1;
    int count2;

    for(int i = 1; i <= n; i++){
        count1 = 0;
        for(int k = 1; k <= n; k++){
            if(i == k) continue;
            if(arr[i][k] != INT_MAX){
                count1++;
            }
        }
        if(count1 >= (n + 1) / 2){
            // cout << i << "count1\n";
            ans++;
        }
    }

    for(int i = 1; i <= n; i++){
        count1 = 0;
        for(int k = 1; k <= n; k++){
            if(i == k) continue;
            if(arr[k][i] != INT_MAX){
                count1++;
            }
        }
        if(count1 >= (n + 1) / 2){
            // cout << i << "count1\n";
            ans++;
        }
    }

    cout << ans;
}