#include <bits/stdc++.h>

// 메모리 초과

using namespace std;

typedef pair<int, int> pa;

struct road;

struct node{
    int val;
    int max_cost;        // cost가 비싸면 roads 없데이트 같으면 roads 추가
    vector<pa> child_list;          // idx, w
    vector<road*> road_list;
    node(int n){
        this->val = n;
        this->max_cost = 0;
    }
};

struct road{
    int s;
    int e;
    road(int x, int y){
        s = x;
        e = y;
    }
};

int cmp(road* x, road* y){
    if(x->s > y->s){
        return 0;
    }
    else if(x->s > y->s){
        return 1;
    }
    else{
        if(x->e > y->e){
            return 0;
        }
        else{
            return 1;
        }
    }
}

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
                dest_node->road_list.clear();
                for(int k = 0; k < cur_node->road_list.size(); k++){
                    dest_node->road_list.push_back(cur_node->road_list[k]);
                }
                dest_node->road_list.push_back(new road(cur_idx, dest));
            }
            else if(dest_node->max_cost == cur_node->max_cost + weight){
                // cout << dest << ": dest " << dest_node->max_cost << "\n";
                // cout << dest_node->roads << " " << cur_node->roads << "\n";
                for(int k = 0; k < cur_node->road_list.size(); k++){
                    dest_node->road_list.push_back(cur_node->road_list[k]);
                }
                dest_node->road_list.push_back(new road(cur_idx, dest));
            }

        }

    }

    // for(int i = 1; i <= n; i++){
    //     cout << i << " i " << node_list[i]->max_cost << " : max_cost " << node_list[i]->roads << " : roads\n";
    // }

    sort(node_list[end]->road_list.begin(), node_list[end]->road_list.end(), cmp);

    int roads = 0;
    int check_x = 0;
    int check_y = 0;

    for(int i = 0; i < node_list[end]->road_list.size(); i++){
        road* cur_road = node_list[end]->road_list[i];
        if(cur_road->s == check_x && cur_road->e == check_y) continue;
        roads++;
        check_x = cur_road->s;
        check_y = cur_road->e;
        // cout << node_list[end]->road_list[i]->s << " " << node_list[end]->road_list[i]->e << "\n";
    }

    cout << node_list[end]->max_cost << "\n";
    cout << roads;

    return 0;
}