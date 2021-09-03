/*
 백준 1679 숫자놀이
 21.09.02
 https://github.com/skyqnaqna/algorithm_study
 */

import Foundation

let n = Int(readLine()!)!
let nums = readLine()!.split(separator: " ").map { Int(String($0))! }
let limit = Int(readLine()!)!

var visited = [Bool](repeating: false, count: 50001) // 최대 숫자 1000, 최대 사용 횟수 50 이므로
    , q = [(num: Int, cnt: Int)]()
    , front = 0

visited[0] = true

// 초기에 주어지는 숫자들은 방문체크해주고 큐에 사용횟수 1과함께 넣어줌
for num in nums {
  visited[num] = true
  q.append((num: num, cnt: 1))
}

while front < q.count {
  let (now, cnt) = q[front]
  front += 1

  // 이미 사용 횟수가 제한에 걸리면 넘어가기
  if limit <= cnt { continue }

  // 현재 숫자에서 방문하지 않은 숫자들을 큐에 넣기
  for num in nums {
    if visited[now + num] { continue }

    // 숫자 하나가 늘어났으므로 cnt + 1을 해줌
    q.append((num: now + num, cnt: cnt + 1))
    visited[now + num] = true
  }
}

for i in visited.indices {
  // 1씩 증가하는데 false라면 이미 누군가 졌다는 것
  if !visited[i] {
    if i % 2 == 0 {
      print("holsoon win at \(i)")
    } else {
      print("jjaksoon win at \(i)")
    }
    break
  }
}