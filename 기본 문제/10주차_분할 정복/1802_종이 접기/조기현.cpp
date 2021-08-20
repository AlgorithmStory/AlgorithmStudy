#include<bits/stdc++.h>
#define f(i,l,r) for(int i=l;i<r;++i)
using namespace std;

string a;

// n길이의 문자열이 가운데 지점을 기준으로 i만큼 떨어진 요소 두가지가 서로 다른지 검사
// 다르다면 한쪽 절반을 같은 방식으로 검사
// 이 과정을 길이가 1이 될 때까지 반복
bool isPossible(int n){
    if(n==1)return true;
    int half=n>>1;
    --n;
    f(i,0,half)if(a[i]==a[n-i])return false;
    return isPossible(half);
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int t;cin>>t;
    while(t--){
        cin>>a;
        cout<<(isPossible(a.length())?"YES":"NO")<<'\n';
    }
    return 0;
}
