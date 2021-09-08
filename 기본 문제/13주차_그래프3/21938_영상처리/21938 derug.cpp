#include<bits/stdc++.h>

using namespace std;

int n, m, t, cnt;
int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};
int mp[1005][1005];


//dfs 탐색 하면서 방문한 곳은 -1로 바꿈

int dfs(int x, int y){
    if(mp[x][y]<3*t) return 0;
    mp[x][y]=-1;
    for(int i=0; i<4; i++){
        int nx=x+dx[i];
        int ny=y+dy[i];
        if(0<=nx&&nx<n&&0<=ny&&ny<m)
            dfs(nx,ny);
    }
    return 1;
}

int main(){
    scanf("%d %d", &n, &m);
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            int a;
            for(int k=0; k<3; k++){
                scanf("%d", &a);
                mp[i][j]+=a;
            }
        }
    }
    scanf("%d", &t);
    
    //영역의 갯수 세어주
  
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            cnt+=dfs(i,j);
        }
    }
    printf("%d", cnt);
}
