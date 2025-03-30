#include <bits/stdc++.h>

using namespace std;
struct node;

typedef pair<int, int> pa;                  // idx, w
typedef pair<node*, int> edge;


struct node{
    int val;
    vector<edge> child_list;
    vector<pa> sub_list;

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
    vector<int> result_list(n+1, 0);
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
        if(cur_node->sub_list.size() == 0){
            for(int i = 0; i < cur_node->child_list.size(); i++){
                int child_idx = cur_node->child_list[i].first->val;
                inner_count[child_idx]--;
                node_list[child_idx]->sub_list.push_back(make_pair(cur_idx, cur_node->child_list[i].second));
                if(inner_count[child_idx] == 0){
                    q.push(child_idx);
                }
            }
        }
        else{
            for(int i = 0; i < cur_node->child_list.size(); i++){
                int child_idx = cur_node->child_list[i].first->val;
                inner_count[child_idx]--;
                if(inner_count[child_idx] == 0){
                    q.push(child_idx);
                }

                for(int j = 0; j < cur_node->sub_list.size(); j++){
                    int push_idx = cur_node->sub_list[j].first;
                    int push_w = cur_node->sub_list[j].second * cur_node->child_list[i].second;
                    node_list[child_idx]->sub_list.push_back(make_pair(push_idx, push_w));
                }
            }
        }

    }

    node* ans_node = node_list[n];
    for(int i = 0; i < ans_node->sub_list.size(); i++){
        int ans_idx = ans_node->sub_list[i].first;
        int ans_w = ans_node->sub_list[i].second;
        result_list[ans_idx] += ans_w;
    }
    for(int i = 1; i <= n; i++){
        if(result_list[i] != 0){
            cout << i << " " << result_list[i] << "\n";
        }
    }



    return 0;
}