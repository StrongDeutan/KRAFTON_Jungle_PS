#include <bits/stdc++.h>

using namespace std;
struct node;

typedef pair<int, int> pa;                  // idx, w
typedef pair<node*, int> edge;

struct node{
    int val;
    vector<edge> child_list;
    unordered_map<int, int> sub_list;

    node(int n){
        this->val = n;
    }
};

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, x, y, k;
    cin >> n >> m;
    vector<node*> node_list(n + 1);
    vector<int> result_list(n + 1, 0);
    for(int i = 1; i <= n; i++){
        node_list[i] = new node(i);
    }
    vector<int> inner_count(n + 1, 0);
    while(m--){
        cin >> x >> y >> k;
        inner_count[x]++;
        node_list[y]->child_list.push_back(make_pair(node_list[x], k));
    }

    queue<int> q;
    for(int i = 1; i <= n; i++){
        if(inner_count[i] == 0){
            q.push(i);
        }
    }

    while(!q.empty()){
        int cur_idx = q.front();
        q.pop();
        node* cur_node = node_list[cur_idx];

        if(cur_node->sub_list.empty()){
            for(auto& child : cur_node->child_list){
                int child_idx = child.first->val;
                inner_count[child_idx]--;
                node_list[child_idx]->sub_list[cur_idx] += child.second;
                if(inner_count[child_idx] == 0){
                    q.push(child_idx);
                }
            }
        } else {
            for(auto& child : cur_node->child_list){
                int child_idx = child.first->val;
                inner_count[child_idx]--;
                if(inner_count[child_idx] == 0){
                    q.push(child_idx);
                }
                for(auto& sub : cur_node->sub_list){
                    node_list[child_idx]->sub_list[sub.first] += sub.second * child.second;
                }
            }
        }
    }

    node* ans_node = node_list[n];
    for(auto& sub : ans_node->sub_list){
        result_list[sub.first] += sub.second;
    }
    for(int i = 1; i <= n; i++){
        if(result_list[i] != 0){
            cout << i << " " << result_list[i] << "\n";
        }
    }

    return 0;
}