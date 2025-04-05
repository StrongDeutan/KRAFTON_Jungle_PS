#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ll;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vector<int> price(n);
        for(int i = 0; i < n; i++){
            cin >> price[i];
        }
        int m;
        cin >> m;
        vector<ll> dp(m + 1, 0);
        dp[0] = 1;
        
		for (int j = 0; j < n; j++) {
			for (int i = 1; i <= m; i++) {
				if (i - price[j] >= 0)
					dp[i] += dp[i - price[j]];
			}
		}

        cout << dp[m] << "\n";
    }


    return 0;
}