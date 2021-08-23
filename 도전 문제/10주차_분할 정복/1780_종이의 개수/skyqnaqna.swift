/*
 백준 1780 종이의 개수
 21.08.22
 https://github.com/skyqnaqna/algorithm_study
 */

import Foundation

let n = Int(readLine()!)!

var graph = [[Int]]()
var ans = [Int](repeating: 0, count: 3)

for _ in 0 ..< n {
  graph.append(readLine()!.split(separator: " ").map { Int(String($0))! })
}

// size x size 크기의 영역이 같은 수로 되어 있다면 true 반환
func check(_ r: Int, _ c: Int, _ size: Int) -> Bool {
  for i in 0 ..< size {
    for j in 0 ..< size {
      if graph[r][c] != graph[r + i][c + j] {
        return false
      }
    }
  }
  return true
}

func divide(_ r: Int, _ c: Int, _ size: Int) {
  if check(r, c, size) {
    ans[graph[r][c] + 1] += 1
  } else {
    // 같은 수로 되어 있지 않다면 9등분하여 탐색
    let oneThird = size / 3
    divide(r, c, oneThird)
    divide(r, c + oneThird, oneThird)
    divide(r, c + oneThird * 2, oneThird)
    divide(r + oneThird, c, oneThird)
    divide(r + oneThird, c + oneThird, oneThird)
    divide(r + oneThird, c + oneThird * 2, oneThird)
    divide(r + oneThird * 2, c, oneThird)
    divide(r + oneThird * 2, c + oneThird, oneThird)
    divide(r + oneThird * 2, c + oneThird * 2, oneThird)
  }
}

divide(0, 0, n)

for res in ans {
  print(res)
}