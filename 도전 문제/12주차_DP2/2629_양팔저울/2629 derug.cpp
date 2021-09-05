#include<bits/stdc++.h>

using namespace std;

int n, m, s;
int d[30050];

int main(){
    int i, j, a;
    scanf("%d", &n);
    d[15000]=1;
    for(i=1; i<=n; i++){
        scanf("%d", &a);
       
        //추가 입력으로 들어 올 때마다 지금까지 측정가능한 무게에서 +, - 해준다.
       
        for(j=s; j>=-s; j--){
            if(0<d[j+15000]&&d[j+15000]<=i){
                if(!d[j+a+15000])
                    d[j+a+15000]=i+1;
                if(!d[j-a+15000])
                    d[j-a+15000]=i+1;
            }
        }
        s+=a;
    }
    scanf("%d", &m);
    for(i=0; i<m; i++){
        scanf("%d", &a);
        if(a<=s&&d[a+15000]) printf("Y ");
        else printf("N ");
    }
}
