// #include <bits/stdc++.h>

// using namespace std;

// int main(){
//     string s;
//     cin >> s;
//     int size_s = s.size();
//     stack<char> stk;
//     int total = 0;
//     bool flag = true;
//     int mult = 1;


//     // - 와 - 사이에 괄호치기
//     for(int i = 0; i < size_s; i++){
//         if(s[i] == '-'){
//             if(flag){
//                 stk.push('(');
//                 flag = false;
//                 stk.push(s[i]);
//             }
//             else{
//                 stk.push(')');
//                 flag = true;
//                 stk.push(s[i]);
//             }
//         }
//         else{
//             stk.push(s[i]);
//         }
        
//     }
//     if(!flag){
//         stk.push(')');
//     }

//     while(!stk.empty()){
//         if(stk.top() == ')'){
//             stk.pop();      // ) 제거
//             while(stk.top() != '('){
//                 if(stk.top() == '+'){
//                     stk.pop();      // + 제거
//                     mult = 1;
//                     continue;
//                 }
//                 total -= (int)(stk.top() - '0') * mult;
//                 mult *= 10;
//                 stk.pop();
//             }
//             stk.pop();      // ( 제거
//             stk.pop();      // - 제거
//             mult = 1;
//         }
//         else{
//             while(!stk.empty() && stk.top() != ')'){
//                 if(stk.top() == '+'){
//                     mult = 1;
//                     stk.pop();
//                     continue;
//                 }
//                 total += (int)(stk.top() - '0') * mult;
//                 mult *= 10;
//                 stk.pop();
//             }
//         }

//     }
//     cout << total;


//     return 0;
// }