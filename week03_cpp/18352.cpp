#include <bits/stdc++.h>

using namespace std;

vector<int> city_list;



struct node{
    int num;
    vector<node*> child_list;
    bool visit;
    node(int n){
        this->num = n;
        this->visit = false;
    }
};

void BFS(node* cur, int k){
    queue<pair<node*, int>> q;
    cur->visit = true;
    pair<node*, int> start = make_pair(cur, 0);
    q.push(start);

    while(!q.empty()){
        pair<node*, int> c = q.front();
        q.pop();
        if(c.second == k){
            city_list.push_back(c.first->num);
        }
        for(int i = 0; i < c.first->child_list.size(); i++){
            if(c.first->child_list[i]->visit == true) continue;
            else{
                pair<node*, int> put = make_pair(c.first->child_list[i], c.second + 1);
                c.first->child_list[i]->visit = true;
                q.push(put);
            }

        }

    }
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k, x;
    cin >> n >> m >> k >> x;

    vector<node*> node_list(n + 1);
    for (int i = 1; i < n + 1; i++){
        node_list[i] = new node(i);
    }

    while(m--){
        int a, b;
        cin >> a >> b;
        node_list[a]->child_list.push_back(node_list[b]);
    }

    BFS(node_list[x], k);

    sort(city_list.begin(), city_list.end());
    
    for (int i = 0; i < city_list.size(); i++){
        cout << city_list[i] << "\n";
    }

    if(city_list.size() == 0){
        cout << -1 << "\n";
    }


    return 0;
}