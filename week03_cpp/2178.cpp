#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    vector<vector<char>> arr(n + 2, vector<char>(m+2, '0'));
    vector<vector<bool>> visit(n + 2, vector<bool>(m+2, true));

    for (int i = 0; i < n; i++){
        string s;
        cin >> s;
        for(int k = 0; k < m; k++){
            arr[i + 1][k + 1] = s[k];
            if(s[k] == '1') visit[i+1][k+1] = false;
        }
    }

    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};


    // <row, col> , depth
    queue<pair<pair<int, int>, int>> q;
    int count = 0;

    pair<pair<int, int>, int> p = make_pair(make_pair(1, 1), 1);
    q.push(p);

    visit[1][1] = true;
    while(!q.empty()){
        count++;
        pair<pair<int, int>, int> cur = q.front();
        if(cur.first.first == n && cur.first.second == m){
            cout << cur.second;
            break;
        }
        q.pop();
        for(int i = 0; i < 4; i++){
            int x = cur.first.first + dx[i];
            int y = cur.first.second + dy[i];
            if(!visit[x][y]){
                visit[x][y] = true;
                pair<int, int> location = make_pair(x, y);
                q.push(make_pair(location, cur.second + 1));
            }
        }



    }



    return 0;
}