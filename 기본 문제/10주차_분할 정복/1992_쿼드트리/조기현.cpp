#include<bits/stdc++.h>
#define f(i,l,r) for(int i=l;i<r;++i)
using namespace std;
char a[64][65];

bool isAllEqual(int r,int c,int n){
    int nr=r+n,nc=c+n;
    f(i,r,nr)f(j,c,nc)if(a[i][j]!=a[r][c])return false;
    return true;
}

// (i,j)를 시작점으로 길이 n인 정사각형에서 압축 결과를 출력
// 모두 같으면 해당 숫자를 출력하고, 다르면 4등분으로 나누어 재귀적으로 진행
void sol(int i,int j,int n){
    if(isAllEqual(i,j,n))cout<<a[i][j];
    else{
        n>>=1;
        cout<<'(';
        sol(i,j,n);
        sol(i,j+n,n);
        sol(i+n,j,n);
        sol(i+n,j+n,n);
        cout<<')';
    }
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int n;cin>>n;
    f(i,0,n)cin>>a[i];
    
    sol(0,0,n);
    
    return 0;
}

