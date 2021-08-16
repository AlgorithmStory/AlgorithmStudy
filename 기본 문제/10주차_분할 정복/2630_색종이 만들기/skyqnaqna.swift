/*
 백준 2630 색종이 만들기
 21.08.16
 https://github.com/skyqnaqna/algorithm_study
 */

import Foundation

// 흰색 파란색 색종이 개수
var white = 0, blue = 0

let n = Int(readLine()!)!
var graph = [[Int]]()

for _ in 0 ..< n {
  graph.append(readLine()!.split(separator: " ").map { Int(String($0))! })
}

// (r, c)를 시작으로 size 크기만큼의 종이가 같은 색으로 이루어졌는지 확인
func checkColor(_ r: Int, _ c: Int, _ size: Int) -> Bool {
  // 크기가 1인 경우 무슨색인지만 확인한다
  if size == 1 {
    if graph[r][c] == 0 {
      white += 1
    } else {
      blue += 1
    }

    return true
  } else {
    // 크기가 1이 아닌 경우,
    // 첫 칸을 기준 색으로 해당 종이가 모두 같은색인지 확인한다
    let color = graph[r][c]

    for i in 0 ..< size {
      for j in 0 ..< size {
        if graph[r + i][c + j] != color {
          return false // 색이 다르므로 false 반환
        }
      }
    }

    // 모두 같은 색이면 해당 색종이 개수 증가
    if color == 0 {
      white += 1
    } else {
      blue += 1
    }
    return true
  }
}

func divide(_ r: Int, _ c: Int, _ size: Int) {
  if checkColor(r, c, size) {
    return
  } else {
    // 색이 다르므로 4등분해서 다시 탐색해준다
    let halfSize = size / 2
    divide(r, c, halfSize)
    divide(r, c + halfSize, halfSize)
    divide(r + halfSize, c, halfSize)
    divide(r + halfSize, c + halfSize, halfSize)
  }
}

divide(0, 0, n)

print(white, blue, separator: "\n")