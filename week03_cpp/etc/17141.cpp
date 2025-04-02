#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> location;

int main(){
    int n, m;
    cin >> n >> m;

    vector<vector<int>> labo(n, vector<int>(n));
    vector<location> locations;
    int total = n*n;
    int wall = 0;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cin >> labo[i][j];
            if(labo[i][j] == 1) wall++;
        }
    }
    bool check = false;               // 모든 경우에 대해 total에 도달하지 못한경우
    total -= wall;

    // -1을 출력하는 경우
    // 바이러스의 갯수가 영역보다 작을 경우
    

    return 0;
}