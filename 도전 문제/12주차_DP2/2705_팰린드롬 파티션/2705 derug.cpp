#include<bits/stdc++.h>

using namespace std;

int dp[1005]={1,1};

//길이가 n일때 갯수를 a_n이라 두면 점화식 a_n=a_n-2+a_[n/2] (n>1, a_0=a_1=1)이 성립하는 것은 쉽게 보일 수 있다.

int f(int n){
    if(dp[n]) return dp[n];
    return dp[n]=f(n-2)+f(n/2);
}

int main(){
    int T;
    scanf("%d", &T);
    while(T--){
        int n;
        scanf("%d", &n);
        printf("%d\n", f(n));
    }
}
