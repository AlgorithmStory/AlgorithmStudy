#include<bits/stdc++.h>
#define f(i,l,r) for(int i=l;i<=r;++i)
using namespace std;
typedef long long ll;

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    ll k;cin>>k;
    ll val=1;
    while(val<=k)val<<=1;   // k보다 큰 2의 배수를 구함
    
    // 매 반복문 마다 k보다 작은 제일 큰 2의 배수(val)를 결정
    // val보다 큰 경우 수의 반전이 일어나므로 체크
    // 이 과정을 k가 1로 도달할 때까지 반복
    int cnt=0;
    while(k>1){
        val>>=1;
        if(k>val)k-=val,++cnt;
    }
    
    cout<<(cnt&1);
    return 0;
}
