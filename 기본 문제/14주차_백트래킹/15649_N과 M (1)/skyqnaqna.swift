/*
 백준 15649 N과 M (1)
 21.09.14
 https://github.com/skyqnaqna/algorithm_study
 */

import Foundation

let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let n = input[0], m = input[1]

// 중복을 피하기 위한 방문체크 배열
var visited = [Bool](repeating: false, count: n + 1)
, answer = ""
, path = [String]() // 수열을 기록할 변수


func recursive(_ cnt: Int) {
  if cnt == m {
    answer += path.joined(separator: " ") + "\n"

    return
  }

  for i in 1 ... n {
    // 방문 안한 숫자는 path에 붙여주고
    if !visited[i] {
      visited[i] = true
      path.append("\(i)")
      recursive(cnt + 1)

      // 재귀에서 빠져나올때 방문했던 수 지워주기
      path.removeLast()
      visited[i] = false
    }
  }
}

recursive(0)
print(answer)