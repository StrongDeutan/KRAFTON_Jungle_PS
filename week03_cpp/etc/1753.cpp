#include <bits/stdc++.h>

using namespace std;

struct vertex;

typedef pair<int, vertex*> edge;

struct vertex{
    vector<edge> edge_list;
    int val;
    vertex(int n){
        this->val = n;
    }
};


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int v, e;
    cin >> v >> e;
    vector<vertex*> vertex_list(v + 1);
    for(int i = 1; i <= v; i++){
        vertex_list[i] = new vertex(i);
    }
    int start;
    cin >> start;
    while(e--){
        int u, v, w;
        cin >> u >> v >> w;
        edge child = make_pair(w, vertex_list[v]);
        vertex_list[u]->edge_list.push_back(child);
    }

    vector<int> dist(v+1, INT_MAX);
    vector<int> status(v+1, 0);

    priority_queue<edge,vector<edge>, greater<edge>> pq;
    dist[start] = 0;
    status[start] = 2;

    for(int i = 0; i < vertex_list[start]->edge_list.size(); i++){
        int child_idx = vertex_list[start]->edge_list[i].second->val;
        dist[child_idx] = min(dist[child_idx], vertex_list[start]->edge_list[i].first);
        status[child_idx] = 1;
        pq.push(make_pair(dist[child_idx], vertex_list[child_idx]));
    }

    while(!pq.empty()){
        auto cur = pq.top();
        pq.pop();
        int weight = cur.first;
        int cur_idx = cur.second->val;
        if(status[cur_idx] == 2){
            continue;
        }
        if(weight > dist[cur_idx]){
            continue;
        }
        
        status[cur_idx] = 2;
        for(int i = 0; i < vertex_list[cur_idx]->edge_list.size(); i++){
            auto& ch = vertex_list[cur_idx]->edge_list[i];
            int we = ch.first;
            int ch_idx = ch.second->val;
            if(status[ch_idx] == 2) continue;
            if(status[ch_idx] == 0){
                dist[ch_idx] = we + dist[cur_idx];
                status[ch_idx] = 1;
                pq.push(make_pair(we + dist[cur_idx], vertex_list[ch_idx]));
            }
            else{
                if(dist[ch_idx] > we + dist[cur_idx]){
                    dist[ch_idx] = we + dist[cur_idx];
                    pq.push(make_pair(we + dist[cur_idx], vertex_list[ch_idx]));
                }
            } 
        }

    }

    for(int i = 1; i <= v; i++){
        if(dist[i] == INT_MAX) cout << "INF\n";
        else cout << dist[i] << "\n";
    }
}