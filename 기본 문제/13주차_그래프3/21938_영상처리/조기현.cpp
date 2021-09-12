#include<bits/stdc++.h>
#define f(i,l,r) for(int i=l;i<r;++i)
using namespace std;

const int MXN=1000,MXM=1000;
int N,M,P[MXN][MXM],T,di[]={0,0,1,-1},dj[]={1,-1,0,0};

// i,j 위치의 RGB 평균값이 T보다 크면 인접한 값을 재귀적으로 검사
// 진행하면서 값을 초기화, 조건 만족 여부에따라 0 or 1 반환
int foo(int i,int j){
    if(i<0||j<0||i>=N||j>=M||(double)P[i][j]/3<T)return 0;
    P[i][j]=0;
    f(d,0,4)foo(i+di[d],j+dj[d]);
    return 1;
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cin>>N>>M;
    f(i,0,N)f(j,0,M){
        int r,g,b;cin>>r>>g>>b;
        P[i][j]=r+g+b;
    }
    cin>>T;
    
    int ans=0;
    f(i,0,N)f(j,0,M)ans+=foo(i,j);
    cout<<ans;
    return 0;
}
