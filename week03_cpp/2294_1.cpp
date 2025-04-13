#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    
    int n, k;
    cin >> n >> k;
    int* price = new int[n];
    int temp;
    for(int i = 0; i < n; i++){
        cin >> price[i];
    }
    queue<pair<int, int>> q;          // val, depth
    for(int i = 0; i < n; i++){
        q.push(make_pair(price[i], 1));
    }
    
    int ans = -1;
    while(!q.empty()){
        if(q.front().first == k){
            ans = q.front().second;
            break;
        }
        for(int i = 0; i < n; i++){
            if(q.front().first+price[i] <= k){
                q.push(make_pair(q.front().first+price[i], q.front().second + 1));
            }
        }
        q.pop();
    }
    cout << ans;


    return 0;
}