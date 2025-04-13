#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    cin >> n;

    vector<int> temp1(501, 0);
    vector<int> temp2(501, 0);
    
    bool flag = true;
    // TRUE -> 1 TO 2  // FALSE -> 2 TO 1

    for(int i = 1; i <= n; i++){
        for (int k = 1; k <= i; k++){
            if(flag){
                cin >> temp1[k];
                if(k == 1){
                    temp1[k] += temp2[1];
                }
                else if(k == i){
                    temp1[k] += temp2[k - 1];
                }
                else{
                    temp1[k] += max(temp2[k - 1], temp2[k]);
                }
            }
            else{
                cin >> temp2[k];
                if(k == 1){
                    temp2[k] += temp1[1];
                }
                else if(k == i){
                    temp2[k] += temp1[k - 1];
                }
                else{
                    temp2[k] += max(temp1[k - 1], temp1[k]);
                }
            }
            
        }
        flag = !flag;
        // for(int p = 1; p <= i; p++){
        //     if(!flag){
        //         cout << temp1[p] << " ";
        //     }
        //     else{
        //         cout << temp2[p] << " ";
        //     }
        // }
        // cout << "\n";
    }

    int ans = 0;

    if(!flag){
        for(int i = 1; i <= n; i++){
            ans = max(ans, temp1[i]);
        }
    }
    else{
        for(int i = 1; i <= n; i++){
            ans = max(ans, temp2[i]);
        }
    }


    cout << ans << "\n";






    return 0;
}