#include <bits/stdc++.h>

using namespace std;

int main(){
    int n, k;
    cin >> n >> k;
    vector<int> coin;
    for(int i = 0; i < n; i++){
        int p;
        cin >> p;
        if(p <= k){
            coin.push_back(p);
        }
    }
    int count = 0;
    int max_idx = coin.size() - 1;
    while(k > 0){
        count += k / coin[max_idx];
        
        // cout << coin[max_idx] << "\n";
        // cout << k / coin[max_idx] << "++\n";
        
        k %= coin[max_idx];

        
        // cout << k << " : k\n";

        while(k < coin[max_idx]){
            max_idx--;
        }

        // cout << coin[max_idx] << " \n";
    }
    cout << count << "\n";




    return 0;
}