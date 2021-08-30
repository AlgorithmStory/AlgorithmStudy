#include<bits/stdc++.h>
#define f(i,l,r) for(int i=l;i<r;++i)
using namespace std;

int arr[10000];

// 전위순회 배열의 l위치에서 r위치까지의 범위에서 후위순회하는 함수.
// 전위순회 배열은 맨 처음이 항상 루트노드이므로,
// 이분탐색을 통해 왼쪽, 오른쪽 자식 노드 경계를 구해 재귀적으로 반복
void sol(int* l,int* r){
    if(l>=r)return;
    int* tmp=upper_bound(l+1,r,*l);
    sol(l+1,tmp);
    sol(tmp,r);
    cout<<*l<<'\n';
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int n=0;
    while(cin>>arr[n++]);
    sol(arr,arr+n-1);
    
    return 0;
}
