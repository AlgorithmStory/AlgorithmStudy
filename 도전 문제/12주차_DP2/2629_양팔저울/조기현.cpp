#include<bits/stdc++.h>
#define f(i,l,r) for(int i=l;i<r;++i)
using namespace std;

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    set<int> s;
    int n;cin>>n;
    // s에 가능한 무게를 모두 저장
    while(n--){
        int num;cin>>num;
        stack<int> tmp;
        for(int ele:s){
            tmp.push(ele+num);
            tmp.push(ele-num);
        }
        while(!tmp.empty()){
            s.insert(tmp.top());
            tmp.pop();
        }
        s.insert(num);
    }
    
    int m;cin>>m;
    while(m--){
        int num;cin>>num;
        cout<<((s.find(num)!=s.end())||(s.find(-num)!=s.end())?'Y':'N')<<' ';
    }
    return 0;
}

