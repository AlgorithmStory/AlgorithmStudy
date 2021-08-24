#include<bits/stdc++.h>
#define f(i,l,r) for(int i=l;i<=r;++i)
using namespace std;

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int N,r,c;cin>>N>>r>>c;
    ++r,++c;
    
    /**
            |
      2사분면 | 1사분면
            |
     --------------
            |
      3사분면 | 4사분면
            |
     
     좌표평면 기준 2사분면에 r,c를 위치하도록 변경하면서 좌,상단 영역의 누적합을 구해나감
     */
    int val=1<<N,ans=0;
    while(r!=1||c!=1){
        int tmp=val*val;
        if(r>val){
            r-=val;
            ans+=tmp<<1;
        }
        if(c>val){
            c-=val;
            ans+=tmp;
        }
        val>>=1;
    }
    cout<<ans;
    
    return 0;
}
