#include<bits/stdc++.h>
#define f(i,l,r) for(int i=l;i<r;++i)
using namespace std;

int N,A[(int)1e5],M;

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int l=0,r=0;
    cin>>N;
    f(i,0,N)cin>>A[i],r=max(r,A[i]);
    cin>>M;
    
    while(l<=r){
        int m=(l+r)>>1,sum=0;
        f(i,0,N)if((sum+=min(m,A[i]))>M)break;
        
        if(sum>M)r=m-1;
        else l=m+1;
    }
    cout<<l-1;
    return 0;
}

