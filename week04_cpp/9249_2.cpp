#include <bits/stdc++.h>
using namespace std;

// 접미사 배열을 더블링 기법으로 구성하는 함수
vector<int> buildSA(const string &s) {
    int n = s.size();
    vector<int> sa(n), rank(n), tmp(n);
    
    // 초기화: 각 위치의 순위는 해당 문자의 아스키 코드값으로 결정
    for (int i = 0; i < n; i++) {
        sa[i] = i;
        rank[i] = s[i];
    }
    
    for (int k = 1; k < n; k *= 2) {
        auto cmp = [&](int i, int j) {
            if (rank[i] != rank[j]) return rank[i] < rank[j];
            int ri = (i + k < n) ? rank[i + k] : -1;
            int rj = (j + k < n) ? rank[j + k] : -1;
            return ri < rj;
        };
        
        sort(sa.begin(), sa.end(), cmp);
        
        tmp[sa[0]] = 0;
        for (int i = 1; i < n; i++) {
            tmp[sa[i]] = tmp[sa[i - 1]] + (cmp(sa[i - 1], sa[i]) ? 1 : 0);
        }
        rank = tmp;
    }
    return sa;
}

// Kasai 알고리즘을 이용한 LCP 배열 구성
vector<int> buildLCP(const string &s, const vector<int> &sa) {
    int n = s.size();
    vector<int> lcp(n, 0), rank(n, 0);
    for (int i = 0; i < n; i++) {
        rank[sa[i]] = i;
    }
    int h = 0;
    for (int i = 0; i < n; i++) {
        if (rank[i] > 0) {
            int j = sa[rank[i] - 1];
            while (i + h < n && j + h < n && s[i + h] == s[j + h])
                h++;
            lcp[rank[i]] = h;
            if (h > 0) h--;
        }
    }
    return lcp;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string A, B;
    cin >> A >> B;
    
    // 두 문자열을 구분자 '$'를 사이에 두고 합칩니다.
    string s = A + "$" + B;
    
    // 접미사 배열과 LCP 배열을 구축
    vector<int> sa = buildSA(s);
    vector<int> lcp = buildLCP(s, sa);
    
    int maxLen = 0;
    string ans = "";
    int n = s.size();
    
    // 합친 문자열에서 A는 인덱스 [0, A.size()-1], 구분자는 A.size(), B는 A.size()+1부터 시작합니다.
    for (int i = 1; i < n; i++) {
        int pos1 = sa[i], pos2 = sa[i - 1];
        // 두 접미사가 서로 다른 원본 문자열에 속하는지 확인:
        // A에 속하는 경우: 인덱스 < A.size()
        // B에 속하는 경우: 인덱스 > A.size() (구분자 인덱스는 제외)
        if ((pos1 < (int)A.size() && pos2 > (int)A.size()) ||
            (pos1 > (int)A.size() && pos2 < (int)A.size())) {
            
            int currLCP = lcp[i];
            if (currLCP > maxLen) {
                maxLen = currLCP;
                // 두 접미사가 공유하는 부분 문자열은 동일하므로 어느 쪽에서 추출해도 무방합니다.
                ans = s.substr(sa[i], currLCP);
            } else if (currLCP == maxLen && maxLen > 0) {
                string candidate = s.substr(sa[i], currLCP);
                if (candidate < ans)
                    ans = candidate;
            }
        }
    }
    
    // 최장 공통 부분 문자열이 없으면 0을 출력
    if (maxLen == 0)
        cout << 0 << "\n";
    else {
        cout << maxLen << "\n" << ans;
    }
    
    return 0;
}
