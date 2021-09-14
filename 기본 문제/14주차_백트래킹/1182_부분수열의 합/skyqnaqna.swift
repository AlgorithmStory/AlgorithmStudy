/*
 백준 1182 부분수열의 합
 21.09.15
 https://github.com/skyqnaqna/algorithm_study
 */

import Foundation

let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let n = input[0], s = input[1]

var arr = readLine()!.split(separator: " ").map { Int(String($0))! }
var answer = 0

// 비트 연산

//모든 경우의 수는 2^n 이고(즉 n개 비트), 크기가 0인 경우는 뺌(빈 수열인 경우)
for i in 1 ..< (1 << n) {
  var sum = 0

  // 수열은 n개 있으니까 0 ~ (n - 1) 인덱스를 비트연산하여 1인 경우만 해당 수열 값 sum에 더하기
  for j in 0 ..< n {
    if i & (1 << j) != 0 {
      sum += arr[j]
    }
  }

  if sum == s {
    answer += 1
  }
}

print(answer)

/*
// 백트래킹 1

var visited = [Bool](repeating: false, count: n)

func recursive(_ idx: Int, _ sum: Int) {
  // 인덱스 범위 넘어가면 리턴
  if idx == n {
    return
  }

  for i in idx ..< n {
    if !visited[i] {
      visited[i] = true

      // 방문 안한건 더할건데, 더했을때 S니??
      if sum + arr[i] == s {
        answer += 1
      }

      recursive(i + 1, sum + arr[i])
      visited[i] = false
    }
  }
}

recursive(0, 0)
print(answer)

// 백트래킹 2

func recursive2(_ idx: Int, _ sum: Int) {
  if idx == n {
    return
  }

  // 지금 idx에 있고 sum에 더한게 S인지 확인
  if sum + arr[idx] == s {
    answer += 1
  }

  // arr[idx]를 더한거랑 안한거랑 Go
  recursive2(idx + 1, sum + arr[idx])
  recursive2(idx + 1, sum)
}

recursive2(0, 0)
print(answer)
 */