#include<bits/stdc++.h>
#define f(i,l,r) for(int i=l;i<=r;++i)
using namespace std;

const int MXN=1e5+1;
int n,a[MXN],ans;
bool chk[MXN];

// i부터 +-a[i] 만큼 방문
void foo(int i){
    if(i<1||i>n||chk[i])return;
    chk[i]=true;
    ++ans;
    foo(i+a[i]);
    foo(i-a[i]);
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cin>>n;
    f(i,1,n)cin>>a[i];
    int s;cin>>s;
    foo(s);
    cout<<ans;
    return 0;
}
