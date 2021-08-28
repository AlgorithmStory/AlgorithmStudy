#include<bits/stdc++.h>
#define f(i,l,r) for(int i=l;i<r;++i)
using namespace std;

const int MXN=10001;
int p[MXN];

// x에 입력받은 노드의 부모를 순서대로 저장
void foo(stack<int> &x){
    int i;cin>>i;
    x.push(i);
    while(p[i]){
        i=p[i];
        x.push(i);
    }
}

void sol(){
    memset(p,0,sizeof(p));
    int n,a,b;
    cin>>n;
    while(--n){
        cin>>a>>b;
        p[b]=a;
    }
    stack<int> s,t;
    foo(s);
    foo(t);
    
    // s,t에 저장된 두 노드의 가장 가까운 공통 부모를 구함
    int ans;
    while(!s.empty()&&!t.empty()&&s.top()==t.top()){
        ans=s.top();
        s.pop();
        t.pop();
    }
    cout<<ans<<'\n';
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int t;cin>>t;
    while(t--)sol();
    return 0;
}
