#include<bits/stdc++.h>
#define f(i,l,r) for(int i=l;i<r;++i)
using namespace std;

int a[2187][2187],ans[3];

bool isAllEqual(int i,int j,int n) {
    int ni=i+n,nj=j+n;
    f(r,i,ni)f(c,j,nj)if(a[r][c]!=a[i][j])return false;
    return true;
}

// (i,j)부터 크기 n인 정사각형 내부가 같은 숫자로 채워져 있는지 검사
// 다르다면 9등분하여 과정 반복
void sol(int i,int j,int n){
    if(isAllEqual(i,j,n)){
        ++ans[a[i][j]+1];
        return;
    }
    int tmp=n/3;
    f(r,0,3)f(c,0,3)sol(i+r*tmp,j+c*tmp,tmp);
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int n;cin>>n;
    f(i,0,n)f(j,0,n)cin>>a[i][j];
    sol(0,0,n);
    f(i,0,3)cout<<ans[i]<<'\n';
    return 0;
}
