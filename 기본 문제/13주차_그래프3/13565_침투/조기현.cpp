#include<bits/stdc++.h>
#define f(i,l,r) for(int i=l;i<r;++i)
using namespace std;

const int MXN=1000;
int M,N,di[]={0,0,-1,1},dj[]={-1,1,0,0};
char p[MXN][MXN+1];

// 바깥쪽에 도달하면 종료
void foo(int i,int j){
    if(i>=M||j<0||j>=N||p[i][j]=='1')return;
    if(i==0){
        cout<<"YES";
        exit(0);
    }
    p[i][j]='1';
    f(d,0,4)foo(i+di[d],j+dj[d]);
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cin>>M>>N;
    f(i,0,M)cin>>p[i];
    
    f(j,0,N)foo(M-1,j);
    cout<<"NO";
    
    return 0;
}

