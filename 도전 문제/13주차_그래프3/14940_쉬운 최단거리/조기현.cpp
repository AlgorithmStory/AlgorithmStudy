#include<bits/stdc++.h>
#define f(i,l,r) for(int i=l;i<r;++i)
using namespace std;

int n,m,p[1000][1000],s[1000][1000],di[]={0,0,-1,1},dj[]={-1,1,0,0};
bool chk[1000][1000];

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    
    queue<pair<int,int>> q;
    cin>>n>>m;
    f(i,0,n)f(j,0,m){
        cin>>p[i][j];
        s[i][j]=(p[i][j]?-1:0);
        if(p[i][j]==2){
            q.push({i,j});
            s[i][j]=0;
            chk[i][j]=true;
        }
    }
    
    // bfs
    int size,dist=1;
    while(size=q.size()){
        while(size--){
            auto &tmp=q.front();
            f(d,0,4){
                int ni=tmp.first+di[d],nj=tmp.second+dj[d];
                if(ni<0||nj<0||ni>=n||nj>=m||chk[ni][nj]||!p[ni][nj])continue;
                chk[ni][nj]=true;
                s[ni][nj]=dist;
                q.push({ni,nj});
            }
            q.pop();
        }
        ++dist;
    }
    
    f(i,0,n){
        f(j,0,m)cout<<s[i][j]<<' ';
        cout<<'\n';
    }
    
    return 0;
}
