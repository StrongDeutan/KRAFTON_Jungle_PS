#include <bits/stdc++.h>

using namespace std;

int ans = 0;
struct location{
    int val;
    int adj_out;
    int adj_in;
    bool visit;
    vector<location*> adj_list;
    location(int n){
        this->val = n;
        this->adj_in = 0;
        this->adj_out = 0;
        this->visit = false;
    }

};





int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<location*> locations(n+1);
    for(int i = 1; i <= n; i++){
        locations[i] = new location(i);
    }
    string s;
    cin >> s;

    for(int i = 0; i < n - 1; i++){
        int u, v;
        cin >> u >> v;

        if(s[v - 1] == '1'){
            locations[u]->adj_in++;
        }
        else{
            locations[u]->adj_out++;
            if(s[u - 1] == '0'){
                locations[u]->adj_list.push_back(locations[v]);
                locations[v]->adj_list.push_back(locations[u]);
            }
        }
        if(s[u - 1] == '1'){
            locations[v]->adj_in++;
        }
        else{
            locations[v]->adj_out++;
        }

    }


   

    for(int i = 1; i <= n; i++){
        location* cur_node = locations[i];
        if(s[i - 1] == '1'){
            int temp = cur_node->adj_in;
            ans += temp;
        }
        else{
            // int temp = cur_node->adj_in * (cur_node->adj_in - 1);
            // ans += temp;
            // 실외 탐색 adj_in 갯수 세서 nP2
            if(!cur_node->visit){
                int temp = 0;
                queue<int> q;
                q.push(i);
                cur_node->visit = true;
                while(!q.empty()){
                    int c = q.front();
                    q.pop();
                    location* current = locations[c];
                    temp += current->adj_in;
                    for(int j = 0; j < current->adj_list.size(); j++){
                        if(!current->adj_list[j]->visit){
                            int next = current->adj_list[j]->val;
                            current->adj_list[j]->visit = true;
                            q.push(next);
                        }
                    }
                }
                ans += temp * (temp - 1);
            }


        }
    }
    

    cout << ans;






    return 0;
}