#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> pa;

struct node{
    int val;
    vector<node*> child_list;

    node(int v){
        this->val = v;
    }
};


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<node*> node_list(n + 1);
    vector<int> inner_count(n + 1, 0);
    queue<int> q;      


    for (int i = 1; i <= n; i++){
        node_list[i] = new node(i);
    }
    for(int i = 0; i < m; i++){
        int a, b;
        cin >> a >> b;

        node_list[a]->child_list.push_back(node_list[b]);
        inner_count[b]++;
    }


    for (int i = 1; i <= n; i++){
        if(inner_count[i] == 0){
            q.push(i);
        }
    }

    while(!q.empty()){
        auto cur_idx = q.front();
        node* cur_node = node_list[cur_idx];
        q.pop();
        for(int i = 0; i < cur_node->child_list.size(); i++){
            int child_idx = cur_node->child_list[i]->val;
            inner_count[child_idx]--;
            if(inner_count[child_idx] == 0){
                q.push(child_idx);
            }
        }
        cout << cur_idx << " ";
    }







    return 0;
}