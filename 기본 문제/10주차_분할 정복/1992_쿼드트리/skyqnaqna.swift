/*
 백준 1992 쿼드트리
 21.08.19
 https://github.com/skyqnaqna/algorithm_study
 */

import Foundation

let n = Int(readLine()!)!

var graph = [[String]]()

for _ in 0 ..< n {
  graph.append(readLine()!.map{ String($0) })
}

// size * size 크기의 사각형 영역이 같은 색으로 이루어졌으면 true 반환
func checkEquality(_ r: Int, _ c: Int, _ size: Int) -> Bool {
  for i in 0 ..< size {
    for j in 0 ..< size {
      if graph[r + i][c + j] != graph[r][c] {
        return false
      }
    }
  }
  return true
}

func quadTree(_ r: Int, _ c: Int, _ size: Int) -> String {
  // 크기가 1이거나 해당 사각형이 같은 색이면 나누어 압축할 필요가 없으므로 해당 색 반환
  if size == 1 || checkEquality(r, c, size) {
    return graph[r][c]
  } else {
    // 색이 다르다면 4등분해서 압축해야하므로 한 변의 크기를 반으로 나눠서
    // 순서대로 탐색한 결과를 res 변수에 추가
    // 이때 res 변수의 앞쪽과 뒷쪽에 괄호를 붙여야 함
    let halfSize = size / 2

    var res = "("
    res += quadTree(r, c, halfSize)
    res += quadTree(r, c + halfSize, halfSize)
    res += quadTree(r + halfSize, c, halfSize)
    res += quadTree(r + halfSize, c + halfSize, halfSize)
    res += ")"

    return res
  }
}

print(quadTree(0, 0, n))