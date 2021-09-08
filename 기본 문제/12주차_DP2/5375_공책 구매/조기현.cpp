#include<bits/stdc++.h>
#define f(i,l,r) for(int i=l;i<r;++i)
#define fr(i,l,r) for(int i=l;i>=r;--i)
using namespace std;

struct info {
    int s,p,o;
    bool operator <(const info &oth) const{
        return p>oth.p;
    }
}a[100];
int s[10001];

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int t;cin>>t;
    while(t--){
        int n,m;cin>>n>>m;
        f(i,0,m)cin>>a[i].s>>a[i].p>>a[i].o;
        sort(a,a+m);    // 공책의 개당 가격을 오름차순으로 정렬
        memset(s,63,sizeof(s));
        s[0]=0;
        // i번째 쇼핑몰의 공책을 최대한 구매했을 때가 공책을 j개 구매할 때의 최적 값일 수 있다.
        // 개당 가격이 i-1번째 쇼핑몰 보다 저렴하기 때문이며,
        // 최적 값이 아닌 경우는 배송비의 영향이므로 이전 최적 값을 유지
        f(i,0,m){
            int val=a[i].s*a[i].p+a[i].o;
            fr(j,n,a[i].s)s[j]=min(s[j],val+s[j-a[i].s]);
            fr(j,a[i].s,1){
                s[j]=min(s[j],val);
                val-=a[i].p;
            }
        }
        cout<<s[n]<<'\n';
    }
    return 0;
}
