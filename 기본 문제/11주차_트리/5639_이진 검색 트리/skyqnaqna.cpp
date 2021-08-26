/*
 백준 5639 이진 검색 트리
 21.08.25
 https://github.com/skyqnaqna/algorithm_study
 */

#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using dd = double;
using pii = pair<int, int>;
using pll = pair<ll, ll>;

#define INF (int)2e9
#define endl "\n"

vector <int> tree;

void pre_to_post(int s, int e) {
    if (s > e) return; // left or right 없는 경우
    if (s == e) { // 리프 노드인 경우
        cout << tree[s] << endl;
        return;
    }

    int root = tree[s];
    int left = s + 1, right = e + 1;

    for (int i = s + 1; i <= e; ++i) {
        if (root < tree[i]) {
            right = i;
            break;
        }
    }

    // root보다 작은 요소들은 left 서브 트리, 큰 요소들은 right 서브 트리로 나눈다
    pre_to_post(left, right - 1);
    pre_to_post(right, e);
    cout << root << endl; // root를 마지막에 출력하여 후위 순회 탐색
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    freopen("input.txt", "r", stdin);

    int n;
    while (cin >> n) {
        tree.push_back(n);
    }

    pre_to_post(0, tree.size() - 1);

    return 0;
}