#include<bits/stdc++.h>
#define f(i,l,r) for(int i=l;i<r;++i)
#define fr(i,l,r) for(int i=l;i>=r;--i)
using namespace std;
int M,N,L[(int)1e6];

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cin>>M>>N;
    f(i,0,N)cin>>L[i];
    
    // 제한 범위 내 (1~10^9) 이분탐색으로 탐색 범위 약 30으로 줄임
    // 과자 개수 N(최대 10^6)번 만큼 순회하면서 기준 값으로 자를 수 있는 과자의 개수 구함
    // 시간 복잡도: N*log(L), 총 연산 회수: 약 10^6 * 30
    int l=1,r=1e9;
    while(l<=r){
        int m=(l+r)>>1,cnt=0;
        fr(i,N-1,0)if((cnt+=L[i]/m)>=M)break;
        if(cnt>=M)l=m+1;
        else r=m-1;
    }
    cout<<l-1;
    
    return 0;
}


