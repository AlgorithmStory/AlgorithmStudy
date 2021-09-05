#include<bits/stdc++.h>

using namespace std;

struct inf{
    int s, p, o;
};

const int MAX=1e9;
int n, m;

bool cmp(inf a, inf b){
    if(a.p==b.p) return a.o<b.o;
    return a.p<b.p;
}

int main(){
    int T;
    scanf("%d", &T);
    while(T--){
        int dp[10005]={};
        inf p[105];

        scanf("%d %d", &n, &m);
        for(int i=1; i<=n; i++)
            dp[i]=MAX;

        for(int i=0; i<m; i++)
            scanf("%d %d %d", &p[i].s, &p[i].p, &p[i].o);
        sort(p,p+m,cmp);

        for(int j=0; j<m; j++){
            for(int i=n; i>=0; i--){
                if(dp[i]!=MAX){
                    int t=min(n-i,p[j].s);
                    dp[i+t]=min(dp[i+t],dp[i]+t*p[j].p+p[j].o);
                }
            }
        }

        printf("%d\n", dp[n]);
    }
}
