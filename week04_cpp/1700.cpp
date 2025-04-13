#include <bits/stdc++.h>

using namespace std;

struct device{
    int count;
    deque<int> idx_list;
    device(){
        this->count = 0;
    }
};


int main(){
    int n, k;
    cin >> n >> k;
    vector<device*> device_list(k + 1);
    for(int i = 1; i <= k; i++){
        device_list[i] = new device();
    }
    vector<int> seq(k);

    for(int i = 0; i < k; i++){
        cin >> seq[i];
        device_list[seq[i]]->count++;
        device_list[seq[i]]->idx_list.push_back(i);
    }   

    vector<int> plug;
    int ans = 0;
    for(int i = 0; i < k; i++){
        
        if(plug.size() < n){
            bool check = false;
            for(int k = 0; k < plug.size(); k++){
                if(plug[k] == seq[i]){
                    check = true;
                    break;
                }
            }
            if(check){
                device_list[seq[i]]->count--;
                device_list[seq[i]]->idx_list.pop_front();
                if(!device_list[seq[i]]->idx_list.size()){
                    device_list[seq[i]]->idx_list.push_back(INT_MAX);
                }
            }
            else{
                plug.push_back(seq[i]);
                device_list[seq[i]]->count--;
                device_list[seq[i]]->idx_list.pop_front();
                if(!device_list[seq[i]]->idx_list.size()){
                    device_list[seq[i]]->idx_list.push_back(INT_MAX);
                }
            }
            
        }
        else{
            bool check = false;
            int max_v = 0;
            int max_i = 0;
            for(int k = 0; k < plug.size(); k++){
                if(plug[k] == seq[i]){
                    check = true;
                }
                if(device_list[plug[k]]->idx_list.front() > max_v)
                {
                    max_v = device_list[plug[k]]->idx_list.front();
                    max_i = k;
                }
            }
            if(check){
                device_list[seq[i]]->count--;
                device_list[seq[i]]->idx_list.pop_front();
                if(!device_list[seq[i]]->idx_list.size()){
                    device_list[seq[i]]->idx_list.push_back(INT_MAX);
                }
            }
            else{
                ans++;
                plug[max_i] = seq[i];
                device_list[seq[i]]->count--;
                device_list[seq[i]]->idx_list.pop_front();
                if(!device_list[seq[i]]->idx_list.size()){
                    device_list[seq[i]]->idx_list.push_back(INT_MAX);
                }
            }
        }

    }


    cout << ans << "\n";
}