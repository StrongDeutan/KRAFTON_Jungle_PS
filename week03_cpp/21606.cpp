#include <bits/stdc++.h>

using namespace std;

int ans = 0;
struct location{
    int val;
    int adj_out;
    int adj_in;
    vector<location*> adj_list;
    location(int n){
        this->val = n;
        this->adj_in = 0;
        this->adj_out = 0;
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
            int temp = cur_node->adj_in * (cur_node->adj_in - 1);
            ans += temp;
            // 실외끼리 BFS
            vector<int> check(n + 1, 0);
            check[cur_node->val] = 1;
            queue<int> q;
            for(int j = 0; j < cur_node->adj_list.size(); j++){
                q.push(cur_node->adj_list[j]->val);
                check[cur_node->adj_list[j]->val] = 1;
            }
            while(!q.empty()){
                int c = q.front();
                q.pop();
                location* c_node = locations[c];
                ans += cur_node->adj_in * c_node->adj_in;
                for(int k = 0; k < c_node->adj_list.size(); k++){
                    int next = c_node->adj_list[k]->val;
                    if(check[next] == 0){
                        check[next] = 1;
                        q.push(next);
                    }
                }
            }

            
        }
    }
    

    cout << ans;






    return 0;
}