#include<bits/stdc++.h>
#define f(i,l,r) for(int i=l;i<r;++i)
using namespace std;

int t=1<<17,s[1<<18][2];

// a<b 인 조건에서 1,2 과정 반복
// 1. a가 홀수, b가 짝수일 때 최대,최소 값 갱신
// 2. a,b 각각 우, 좌로 이동하여 2로 나눈 값으로 갱신
// a==b 인 경우에 최대, 최소 값 갱신
void sol(){
    int a,b;cin>>a>>b;
    --a+=t;--b+=t;
    int mn=1e9,mx=0;
    while(a<b){
        if(a&1)mn=min(mn,s[a][0]),mx=max(mx,s[a][1]);
        if(!(b&1))mn=min(mn,s[b][0]),mx=max(mx,s[b][1]);
        a=(a+1)>>1;b=(b-1)>>1;
    }
    if(a==b)mn=min(mn,s[a][0]),mx=max(mx,s[a][1]);
    cout<<mn<<' '<<mx<<'\n';
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int n,m;cin>>n>>m;
    f(i,0,n){
        int tmp;cin>>tmp;
        int j=i+t;
        while(j){
            int &mn=s[j][0],&mx=s[j][1];
            mn=mn?min(mn,tmp):tmp;
            mx=mx?max(mx,tmp):tmp;
            j>>=1;
        }
    }
    while(m--)sol();
    return 0;
}
