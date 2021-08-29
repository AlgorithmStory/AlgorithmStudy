import Foundation

let n = Int(readLine()!)!
var arr = (0..<n).map { _ in Array(readLine()!.split(separator: " ").suffix(from: 1)) }

// 철자 순 정렬
arr.sort { a, b in
    for i in 0..<min(a.count, b.count) where a[i] != b[i] {
        return a[i] < b[i]
    }
    return a.count < b.count
}

// 출력
var visited: [String.SubSequence] = (0..<16).map { _ in "" }
arr.forEach {
    $0.enumerated().forEach { idx, room in
        guard visited[idx] != room else { return }
        visited[idx + 1] = ""
        visited[idx] = room
        print(String(repeating: "--", count: idx), room, separator: "")
    }
}

