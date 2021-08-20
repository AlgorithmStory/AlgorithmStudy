/*
 백준 18222 투에-모스 문자열
 21.08.19
 https://github.com/skyqnaqna/algorithm_study
 */

import Foundation

// 1번째는 0이므로 k - 1을 해준 값의 이진수를 구한다
let k = String(Int(readLine()!)! - 1, radix: 2)
var count = 0

// 값이 1인 비트의 수를 센다
for bit in k {
  if bit == "1" {
    count += 1
  }
}

if count % 2 == 0 {
  print(0)
} else {
  print(1)
}