#include <bits/stdc++.h>

using namespace std;

typedef tuple<int, int, bool> grade;

int cmp(grade x, grade y){
    if(get<0>(x) < get<0>(y)){
        return 1;
    }
    else{
        return 0;
    }
}
int cmp2(grade x, grade y){
    if(get<1>(x) < get<1>(y)){
        return 1;
    }
    else{
        return 0;
    }
}


int main(){
    ios_base::sync_with_stdio(false);
    
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vector<grade> g1(n);
        vector<grade> g2(n);
        for(int i = 0; i < n; i++){
            int a, b;
            cin >> a >> b;
            g1[i] = make_tuple(a, b, false);
            g2[i] = make_tuple(a, b, false);
        }

        sort(g1.begin(), g1.end(), cmp);
        sort(g2.begin(), g2.end(), cmp2);

        // cout << "\n";
        
        // for(int i = 0; i < n; i++){
        //     cout << apply[i].first << " " << apply[i].second << "\n";
        // }
        // cout << "\n";

        int count = 0;

        for(int i = 0; i < n; i++){
            if(get<2>(g1[i])) continue;
            int cur_y = get<1>(g1[i]);
            get<2>(g1[i]) = true;
            get<2>(g2[cur_y - 1]) = true;
            for(int j = cur_y; j < n; j++){
                if(get<2>(g2[j])){
                    break;
                }
                get<2>(g2[j]) = true;
                // cout << get<0>(g2[j]) << " " << get<1>(g2[j]) << " " << i << " " << j << " count\n";
                count++;
                get<2>(g1[get<0>(g2[j]) - 1]) = true;
            }
            // cout << count << "\n";
        }
        cout << n - count << "\n";
    }





    return 0;
}