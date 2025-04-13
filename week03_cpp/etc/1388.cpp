#include <bits/stdc++.h>

using namespace std;

int main(){
    int n, m;
    cin >> n >> m;
    vector<vector<char>> mat(n, vector<char>(m));
    vector<vector<bool>> check(n, vector<bool>(m, false));
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> mat[i][j];
        }
    }

    int ans = 0;
    


    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(!check[i][j]){
                ans++;
            }
            check[i][j] = true;
            if(mat[i][j] == '-'){
                for(int k = j+1; k < m; k++){
                    if(mat[i][k] == '-'){
                        check[i][k] = true;
                    }
                    else{
                        break;
                    }
                }
            }
            else{
                for(int k = i+1; k < n; k++){
                    if(mat[k][j] == '|'){
                        check[k][j] = true;
                    }
                    else{
                        break;
                    }
                }
            }
        }
    }

    cout << ans;


    return 0;
}