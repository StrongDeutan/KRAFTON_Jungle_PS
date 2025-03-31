#include <bits/stdc++.h>

using namespace std;

typedef unsigned short uss;
typedef pair<uss, uss> pa;

struct node{
    int val;
    int max_cost;        // cost가 비싸면 roads 없데이트 같으면 roads 추가
    vector<pa> child_list;          // idx, w
    set<pa> road_list;

    node(int n){
        this->val = n;
        this->max_cost = 0;
    }
};



int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<node*> node_list(n+1);
    vector<uss> inner_count(n+1, 0);

    for(int i = 1; i<= n; i++){
        node_list[i] = new node(i);
    }

    while(m--){
        uss s, e, w;
        cin >> s >> e >> w;
        inner_count[e]++;
        node_list[s]->child_list.push_back(make_pair(e, w));
    }

    queue<uss> q;
    uss start, end;
    cin >> start >> end;
    q.push(start);

    while(!q.empty()){
        uss cur_idx = q.front();
        q.pop();
        node* cur_node = node_list[cur_idx];
        for(int i = 0; i < cur_node->child_list.size(); i++){
            auto child = cur_node->child_list[i];
            uss dest = child.first;
            uss weight = child.second;
            inner_count[dest]--;
            if(inner_count[dest] == 0){
                q.push(dest);
            }
            node* dest_node = node_list[dest];
            if(dest_node->max_cost < cur_node->max_cost + weight){
                dest_node->max_cost = cur_node->max_cost + weight;
                dest_node->road_list.clear();
                for(auto& s : cur_node->road_list){
                    dest_node->road_list.insert(s);
                }
                dest_node->road_list.insert(make_pair(cur_idx, dest));
            }
            else if(dest_node->max_cost == cur_node->max_cost + weight){
                for(auto& s : cur_node->road_list){
                    dest_node->road_list.insert(s);
                }
                dest_node->road_list.insert(make_pair(cur_idx, dest));
            }
            

        }

    }

    // for(int i = 1; i <= n; i++){
    //     cout << i << " i " << node_list[i]->max_cost << " : max_cost " << node_list[i]->roads << " : roads\n";
    // }

    cout << node_list[end]->max_cost << "\n";
    cout << node_list[end]->road_list.size() << "\n";
    return 0;
}