#include <bits/stdc++.h>

using namespace std;

typedef tuple<int, int, int, int> tp; // 시작, 끝, 강의번호, index

int cmp(tp x, tp y){
    int xv = get<0>(x);
    int yv = get<0>(y);

    if(xv < yv){
        return 1;
    }
    else if(xv > yv){
        return 0;
    }
    else{
        if(get<1>(x) < get<1>(y)){
            return 1;
        }
        else{
            return 0;
        }
    }

}



int main(){
    int n;
    cin >> n;
    vector<tp> lec_list(n);
    for(int i = 0; i < n; i++){
        int num, s, e;
        cin >> num >> s >> e;
        lec_list[i] = make_tuple(s, e, num, i);
    }

    sort(lec_list.begin(), lec_list.end(), cmp);

    for(int i = 0; i < n; i++){
        cout << get<0>(lec_list[i]) << " " << get<1>(lec_list[i]) << " " << get<2>(lec_list[i]) << "\n";
    }
    priority_queue<tp, vector<tp>, greater<tp>> pq;
    




    return 0;
}