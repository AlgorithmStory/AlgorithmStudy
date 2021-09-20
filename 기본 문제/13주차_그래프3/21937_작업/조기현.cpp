#include<bits/stdc++.h>
#define f(i,l,r) for(int i=l;i<r;++i)
using namespace std;

const int MXN=1e5+1;
vector<int> edge[MXN];
bool chk[MXN];

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int n,m;cin>>n>>m;
    f(i,0,m){
        int a,b;cin>>a>>b;
        edge[b].push_back(a);
    }
    int x;cin>>x;
    
    int ans=0;
    stack<int> s;
    s.push(x);
    // bfs 수행
    while(!s.empty()){
        int i=s.top();
        s.pop();
        
        for(int j:edge[i])if(!chk[j]){
            chk[j]=true;
            ++ans;
            s.push(j);
        }
    }
    cout<<ans;
    
    return 0;
}

