#include <bits/stdc++.h>
using namespace std;
struct node;
struct edge;
typedef pair<int, int> pa;
struct edge{
    int s;
    int e;
    int w;
    edge(int s, int e, int w){
        this->s = s;
        this->e = e;
        this->w = w;
    }

};

struct node{
    bool visit;
    int val;
    deque<edge*> edges;                      // 맨 앞이 가장 낮은 간선 보장
    node(int v){
        this->val = v;
        this->visit = false;
    }
};

class graph{
    public:
        graph(int n, int m, int k){
            this->n = n;
            this->m = m;
            this->k = k;
            node_list.push_back(nullptr);
            for(int i = 0; i < k; i++){
                result.push_back(0);
            }
            for(int i = 1; i <= n; i++){
                node* new_node = new node(i);
                node_list.push_back(new_node);
            }
            for(int i = 1; i <= m; i++){
                int s, e;
                cin >> s >> e;
                edge* new_edge1 = new edge(s, e, i);
                edge* new_edge2 = new edge(e, s, i);
                edge_list.push_back(new_edge1);
                node_list[s]->edges.push_back(new_edge1);
                node_list[e]->edges.push_back(new_edge2);
            }
        }

        int prim(){
            int count = 1;
            int total = 0;
            priority_queue<pa, vector<pa>, greater<pa>> pq;
            node* start = this->node_list[1];
            start->visit = true;
            for(int i = 0; i < start->edges.size(); i++){
                pa temp = make_pair(start->edges[i]->w, start->edges[i]->e);
                pq.push(temp);
            }


            while(!pq.empty()){
                pa cur = pq.top();
                
                node* dest = node_list[cur.second];
                pq.pop();
                
                if(dest->visit){
                    continue;
                }
                count++;
                total += cur.first;
                dest->visit = true;
                for(int i = 0; i < dest->edges.size(); i++){
                    pa temp = make_pair(dest->edges[i]->w, dest->edges[i]->e);
                    pq.push(temp);
                }
            }

            if(count == n){
                return total;
            }
            else{
                return 0;
            }
        }

        void init_visit(){
            for(int i = 1; i <= n; i++){
                node_list[i]->visit = false;
            }
        }

        void mst_game(){
            for(int i = 0; i < k; i++){
                int ans = prim();
                if(ans == 0){
                    break;
                }
                result[i] = ans;
                edge* del_edge = edge_list[0];
                node_list[del_edge->s]->edges.pop_front();
                node_list[del_edge->e]->edges.pop_front();
                edge_list.pop_front();
                delete del_edge;

                init_visit();
            }

            for(int i = 0; i < k; i++){
                cout << result[i] << " ";
            }
        }



    private:
        int n;
        int m;
        int k;
        vector<node*> node_list;
        deque<edge*> edge_list;
        vector<int> result;
};




int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    cin >> n >> m >> k;
    
    graph* a = new graph(n, m, k);
    a->mst_game();






    return 0;
}