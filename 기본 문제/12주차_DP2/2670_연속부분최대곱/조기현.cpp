#include<bits/stdc++.h>
#define f(i,l,r) for(int i=l;i<r;++i)
using namespace std;

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int n;
    double prev;
    cin>>n>>prev;
    double ans=prev;
    // 이전의 최대 곱값과 곱한 것과 현재 값을 비교하여, i번째 최대 곱 및 정답 갱신
    while(--n){
        double curr;cin>>curr;
        prev*=curr;
        prev=max(prev,curr);
        ans=max(ans,prev);
    }
    printf("%.3f",round(ans*1000)/1000);
    
    return 0;
}
