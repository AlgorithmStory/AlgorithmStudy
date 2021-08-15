/*
 백준 2512 예산
 21.08.14
 https://github.com/skyqnaqna/algorithm_study
 */

import Foundation

let n = Int(readLine()!)!
var region = readLine()!.split(separator: " ").map { Int(String($0))! }
let m = Int(readLine()!)!

// 예산이 충분하다면 최댓값 출력
if region.reduce(0, +) <= m {
  print(region.max()!)
} else {
  // 예산이 부족하면 1 ~ m 범위로 이분탐색하여 상한액의 최댓값 구하기
  var left = 1, right = m, ans = 0

  while left <= right {
    let mid = (left + right) / 2

    var sum = 0
    for request in region {
      if request > mid {
        sum += mid
      } else {
        sum += request
      }
    }

    if sum > m {
      right = mid - 1
    } else {
      left = mid + 1
      ans = mid
    }
  }

  print(ans)
}
