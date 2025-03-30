#include <bits/stdc++.h>

using namespace std;

struct city{
    int num;
    vector<pair<int, city*>> child_list;     // <가중치, 도착지>
    city(int n){
        this->num = n;
    }
};


void daijkstra(city* start, city* find, vector<int> &distance, vector<int> &visit){
    priority_queue<pair<int, city*>> pq;
    int s = start->num;
    distance[s] = 0;
    visit[s] = 2;
    if(find->num == s){
        cout << distance[s];
        return;
    }

    for (int i = 0; i < start->child_list.size(); i++){
        int idx = start->child_list[i].second->num;
        if(visit[idx] == 2) continue;
        if(visit[idx] == 1){
            distance[idx] = min(distance[idx], -start->child_list[i].first);
            pq.push(make_pair(-distance[idx], start->child_list[i].second));
        }
        else{
            visit[idx] = 1;
            distance[idx] = -start->child_list[i].first;
            pq.push(start->child_list[i]);
        }
        
    }

    while(!pq.empty()){
        pair<int, city*> cur = pq.top();
        pq.pop();
        int idx = cur.second->num;
        int weight = -cur.first;
        if(visit[idx] == 2) continue;
        if(weight > distance[idx]) continue;

        visit[idx] = 2;
        if(cur.second == find){
            cout << distance[idx];
            break;
        }
        for (int i = 0; i < cur.second->child_list.size(); i++){
            pair<int, city*> child = cur.second->child_list[i];
            int child_idx = child.second->num;
            if(visit[child_idx] == 2) continue;
            if(visit[child_idx] == 1){
                if(distance[child_idx] > distance[idx] + (-child.first)){
                    distance[child_idx] = distance[idx] + (-child.first);
                }
                pq.push(make_pair(-distance[child_idx], child.second));
            }
            else{
                distance[child_idx] = distance[idx] + (-child.first);
                pq.push(make_pair(-distance[child_idx], child.second));
            }
            visit[child_idx] = 1;
        }
    }
}



int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<city*> city_list(n + 1);
    vector<int> distance(n + 1, INT_MAX);
    vector<int> visit(n + 1, 0);

    for (int i = 1; i < n + 1; i++){
        city_list[i] = new city(i);
    }

    while(m--){
        int s, e, w;
        cin >> s >> e >> w;
        pair<int, city*> child = make_pair(-w, city_list[e]);
        city_list[s]->child_list.push_back(child);
    }

    int start, end;
    cin >> start >> end;
// ----------------------입력----------------

    daijkstra(city_list[start], city_list[end], distance, visit);




    return 0;
}