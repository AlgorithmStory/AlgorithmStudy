/*
 백준 1074 Z
 21.08.23
 https://github.com/skyqnaqna/algorithm_study
 */

import Foundation

let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let n = input[0], r = input[1], c = input[2]

func recursion(_ n: Int, _ r: Int, _ c: Int) -> Int {
  if n == 0 { return 0 } // n이 0이면 크기가 1인 사각형이므로 0번째임

  let half = 1 << (n - 1) // 사각형 한변의 길이
  /*
   [1] = half x half
        |
    [1] | [2]
  ------+------
    [3] | [4]
        |
   */
  // [1]에 위치하면 2^(n-1) * 2^(n-1) 크기인 사각형 안에서 다시 탐색
  if r < half && c < half { return recursion(n - 1, r, c) }
  // [2]에 위치하면 [1]의 크기인 half * half 만큼 더하고 [2]에서 다시 탐색
  else if r < half && c >= half { return half * half + recursion(n - 1, r, c - half) }
  // [3]에 위치하면 half * half 크기가 이미 두번 지나왔으므로 그만큼 더해주고 탐색
  else if r >= half && c < half { return half * half * 2 + recursion(n - 1, r - half, c) }
  // [4]에 위치하면 마찬가지로 누적된 개수 더해주고 탐색
  else { return half * half * 3 + recursion(n - 1, r - half, c - half) }
}

print(recursion(n, r, c))
