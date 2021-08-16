import Foundation

// p배열의 (i, j)을 시작점으로 n 길이의 정사각형 범위 내 요소가 모두 같은지 여부 반환
func isEqual(_ i: Int, _ j: Int, _ n: Int) -> Bool {
    for r in i..<i+n {
        for c in j..<j+n {
            if p[r][c] != p[i][j] {
                return false
            }
        }
    }
    return true
}

// (i, j)를 시작점으로 n길이를 갖는 정사각형 범위 내에서 자를 수 있는 색종이의 개수를 구함
func sol(_ i: Int, _ j: Int, _ n: Int) {
    if isEqual(i, j, n) {
        ans[p[i][j]] += 1
    } else {
        let m = n / 2
        sol(i, j, m)
        sol(i + m, j, m)
        sol(i, j + m, m)
        sol(i + m, j + m, m)
    }
}


let n = Int(readLine()!)!
let p = (0..<n).map { _ in readLine()!.components(separatedBy: " ").map({ Int($0)! }) }
var ans = [0, 0]
sol(0, 0, n)
print(ans[0], ans[1], separator: "\n")
