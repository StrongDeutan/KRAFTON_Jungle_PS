#include <bits/stdc++.h>

using namespace std;

typedef tuple<int, int, int, int> tp; // x, y, 벽 부순 여부, 거리

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<vector<int>> maps(n, vector<int>(m, 0));
    vector<vector<vector<bool>>> visit(n, vector<vector<bool>>(m, vector<bool>(2, false)));

    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < m; j++) {
            maps[i][j] = s[j] - '0';
        }
    }

    queue<tp> q;
    q.push({0, 0, 0, 1}); // 시작점 (x=0, y=0, 벽 안 부숨, 거리=1)
    visit[0][0][0] = true;

    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};

    while (!q.empty()) {
        auto [x, y, broken, dist] = q.front();
        q.pop();

        // 도착 지점이면 거리 출력 후 종료
        if (x == n - 1 && y == m - 1) {
            cout << dist;
            return 0;
        }

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;

            // 벽이 아닌 경우
            if (maps[nx][ny] == 0 && !visit[nx][ny][broken]) {
                visit[nx][ny][broken] = true;
                q.push({nx, ny, broken, dist + 1});
            }

            // 벽이지만, 아직 부술 기회가 남아 있는 경우
            if (maps[nx][ny] == 1 && broken == 0 && !visit[nx][ny][1]) {
                visit[nx][ny][1] = true;
                q.push({nx, ny, 1, dist + 1});
            }
        }
    }

    // 도착 불가능한 경우
    cout << -1;
    return 0;
}
