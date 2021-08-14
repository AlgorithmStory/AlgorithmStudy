/*
 백준 10828 스택
 21.08.04
 https://github.com/skyqnaqna/algorithm_study
 */

import Foundation

struct Stack {
  private var arr = [Int]()

  public var isEmpty: Int{
    return arr.isEmpty ? 1 : 0
  }

  public var size: Int {
    return arr.count
  }

  public var top: Int {
    guard !arr.isEmpty else {
      return -1
    }

    return arr.last!
  }

  public mutating func push(_ element: Int) {
    arr.append(element)
  }

  public mutating func pop() -> Int {
    guard !arr.isEmpty else {
      return -1
    }

    return arr.removeLast()
  }
}

let n = Int(readLine()!)!

var s = Stack()

for _ in 0 ..< n {
  let inst = readLine()!.split(separator: " ").map{ String($0) }

  if inst[0] == "push" {
    s.push(Int(inst[1])!)
  } else if inst[0] == "top" {
    print(s.top)
  } else if inst[0] == "size" {
    print(s.size)
  } else if inst[0] == "empty" {
    print(s.isEmpty)
  } else if inst[0] == "pop" {
    print(s.pop())
  }
}