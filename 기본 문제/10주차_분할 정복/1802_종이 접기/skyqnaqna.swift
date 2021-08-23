/*
 백준 1802 종이 접기
 21.08.20
 https://github.com/skyqnaqna/algorithm_study
 */

import Foundation

var t = Int(readLine()!)!
var ans = ""

// 중심을 기준으로 접어서 포갤수 있는지 확인
func checkFold(_ left: Int, _ right: Int, _ arr: [Int]) -> Bool {
  if left == right { return true } // 이 부분을 빼먹어서 오래걸림
  var l = left, r = right, mid = (left + right) / 2

  while l < mid && mid < r {
    if arr[l] == arr[r] {
      return false // 반대편이 같다는 것은 mid를 중심으로 접을 때 서로 포갤수 없다는 것
    }
    l += 1
    r -= 1
  }

  // 현재 접을 수 있다면 계속 접을 수 있는지 확인
  return checkFold(left, mid - 1, arr) && checkFold(mid + 1, right, arr)
}

while t > 0 {
  t -= 1

  let paper = readLine()!.map { Int(String($0))! }

  if checkFold(0, paper.count - 1, paper) {
    ans += "YES\n"
  } else {
    ans += "NO\n"
  }
}

print(ans)