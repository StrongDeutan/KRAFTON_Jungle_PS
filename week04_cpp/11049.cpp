#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<pair<int, int>> mat(n);
    for (int i = 0; i < n; ++i) {
        cin >> mat[i].first >> mat[i].second;
    }

    vector<vector<int>> dp(n, vector<int>(n, 0));     // 대각선초기화

    for (int s_col = 2; s_col <= n; s_col++) {
        for (int i = 0; i <= n - s_col; ++i) {
            int j = i + s_col - 1;
            dp[i][j] = INT_MAX;
            for (int k = i; k < j; ++k) {
                dp[i][j] = min(dp[i][j],
                    dp[i][k] + dp[k + 1][j] + mat[i].first * mat[k].second * mat[j].second);
            }
        }
    }

    cout << dp[0][n - 1] << "\n";
}
