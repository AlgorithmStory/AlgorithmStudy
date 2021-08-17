/*
 백준 17829 222-풀링
 21.08.17
 https://github.com/skyqnaqna/algorithm_study
 */

import Foundation

let n = Int(readLine()!)!
var graph = [[Int]]()

// 시간초과 발생
// var graph = (0..<n).map { _ in readLine()!.components(separatedBy: " ").map { Int($0)! }}
for _ in 0 ..< n {
  graph.append(readLine()!.split(separator: " ").map { Int(String($0))! })
}

// 좌상단을 각 정사각형의 시작점으로 두고 2번째로 큰 수를 찾아서 시작점에 저장한다
func pooling(_ r: Int, _ c: Int, _ size: Int) {
  let preSize = size / 2

  // fourNums[0] >= [1] >= [2] >= [3]
  var fourNums = [graph[r][c], graph[r][c + preSize], graph[r + preSize][c], graph[r + preSize][c + preSize]].map { $0 }.sorted(by: > )

  // 2번째로 큰 수 좌상단에 저장
  graph[r][c] = fourNums[1]
}

var size = 2
while size <= n {
  for i in stride(from: 0, through: n - size, by: size) {
    for j in stride(from: 0, through: n - size, by: size) {
      pooling(i, j, size)
    }
  }
  size <<= 1 // 사각형의 크기는 2제곱씩
}

print(graph[0][0])