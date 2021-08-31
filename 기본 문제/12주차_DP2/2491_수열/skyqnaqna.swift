/*
 백준 2491 수열
 21.08.30
 https://github.com/skyqnaqna/algorithm_study
 */

import Foundation

let n = Int(readLine()!)!
let arr = readLine()!.split(separator: " ").map { Int(String($0))! }

// dp[0] : 작아지는 수열의 길이
// dp[1] : 커지는 수열의 길이
var dp = [[Int]](repeating: [Int](repeating: 1, count: n), count: 2)
var ans = 1

for i in 1 ..< n {
  if arr[i] <= arr[i - 1] {
    dp[0][i] = dp[0][i - 1] + 1
  }

  if arr[i] >= arr[i - 1] {
    dp[1][i] = dp[1][i - 1] + 1
  }

  ans = max(ans, max(dp[0][i], dp[1][i]))
}

print(ans)