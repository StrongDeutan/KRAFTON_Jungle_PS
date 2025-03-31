#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> pa;

struct node{
    int val;
    int max_cost;        // cost가 비싸면 roads 없데이트 같으면 roads 추가
    vector<pa> child_list;          // idx, w
    vector<pa> r_child_list;          // idx, w reverse
    bool visit;
    node(int n){
        this->val = n;
        this->max_cost = 0;
        this->visit = false;
    }
};



int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<node*> node_list(n+1);
    vector<int> inner_count(n+1, 0);

    for(int i = 1; i<= n; i++){
        node_list[i] = new node(i);
    }

    while(m--){
        int s, e, w;
        cin >> s >> e >> w;
        inner_count[e]++;
        node_list[s]->child_list.push_back(make_pair(e, w));
        node_list[e]->r_child_list.push_back(make_pair(s, w));
    }

    queue<int> q;
    int start, end;
    cin >> start >> end;
    q.push(start);

    while(!q.empty()){
        int cur_idx = q.front();
        q.pop();
        node* cur_node = node_list[cur_idx];
        for(int i = 0; i < cur_node->child_list.size(); i++){
            auto child = cur_node->child_list[i];
            int dest = child.first;
            int weight = child.second;
            inner_count[dest]--;
            if(inner_count[dest] == 0){
                q.push(dest);
            }
            node* dest_node = node_list[dest];
            if(dest_node->max_cost < cur_node->max_cost + weight){
                dest_node->max_cost = cur_node->max_cost + weight;
            }
        }

    }

    int roads = 0;

    q.push(end);                // 역방향 bfs     max_cost, w 차이로 경로 count
    while(!q.empty()){
        int cur_idx = q.front();
        q.pop();
        node* cur_node = node_list[cur_idx];
        int cur_cost = cur_node->max_cost;
        for(int i = 0; i < cur_node->r_child_list.size(); i++){
            auto child = cur_node->r_child_list[i];
            int dest = child.first;
            int weight = child.second;
            if(cur_cost - weight == node_list[dest]->max_cost){
                roads++;
                if(node_list[dest]->visit){
                    continue;
                }
                node_list[dest]->visit = true;
                q.push(dest);
            }
        }

    }



    // for(int i = 1; i <= n; i++){
    //     cout << i << " i " << node_list[i]->max_cost << " : max_cost " << node_list[i]->roads << " : roads\n";
    // }

    cout << node_list[end]->max_cost << "\n";
    cout << roads;
    return 0;
}