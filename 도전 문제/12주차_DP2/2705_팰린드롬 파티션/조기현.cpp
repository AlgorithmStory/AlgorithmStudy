#include<bits/stdc++.h>
#define f(i,l,r) for(int i=l;i<r;++i)
using namespace std;

int s[1001];

// i의 재귀적인 팰린트롬 파티션 개수 반환
int sol(int n){
    int &ref=s[n];
    if(ref!=-1)return ref;
    ref=1;
    
    f(i,0,n)if((n-i)%2==0)ref+=sol((n-i)>>1);
    return ref;
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    memset(s,-1,sizeof(s));
    int t;cin>>t;
    while(t--){
        int n;cin>>n;
        cout<<sol(n)<<'\n';
    }
    return 0;
}

