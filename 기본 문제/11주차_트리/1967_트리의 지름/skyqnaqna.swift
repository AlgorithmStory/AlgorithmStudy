/*
 백준 1967 트리의 지름
 21.08.27
 https://github.com/skyqnaqna/algorithm_study
 */

import Foundation

let n = Int(readLine()!)!

var nodes = [[(next: Int, w: Int)]](repeating: [(Int, Int)](), count: n + 1)
var visited = [Bool](repeating: false, count: n + 1)

// 가정 먼 거리와 가장 먼 노드
var ans = 0, farNode = 0

for _ in 0 ..< n - 1 {
  let edge = readLine()!.split(separator: " ").map { Int(String($0))! }
  let u = edge[0], v = edge[1], w = edge[2]

  nodes[u].append((v, w))
  nodes[v].append((u, w))
}

func dfs(_ now: Int, _ dist: Int) {
  if dist > ans {
    ans = dist
    farNode = now
  }

  for node in nodes[now] {
    if !visited[node.next] {
      visited[node.next] = true
      dfs(node.next, dist + node.w)
      visited[node.next] = false
    }
  }
}

// 아무 점에서 시작해서 가장 먼 노드를 구한다
visited[1] = true
dfs(1, 0)
ans = 0

// 다시 ans와 vistied를 초기화하고 이전에 구한 노드에서 시작하여 가장 먼 노드를 구한다
visited = [Bool](repeating: false, count: n + 1)
visited[farNode] = true
dfs(farNode, 0)

print(ans)