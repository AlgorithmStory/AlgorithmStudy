#include<bits/stdc++.h>
#define f(i,l,r) for(int i=l;i<r;++i)
using namespace std;

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int n,prev,len[2]={1,1},ans=1;
    cin>>n>>prev;
    // 이전 값과 현재 값을 비교하여 길이 갱신
    while(--n){
        int curr;cin>>curr;
        
        len[0]=1+(prev<=curr?len[0]:0);
        len[1]=1+(prev>=curr?len[1]:0);
        
        prev=curr;
        ans=max(ans,max(len[0],len[1]));
    }
    cout<<ans;
    return 0;
}
