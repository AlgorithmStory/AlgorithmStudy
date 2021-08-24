/*
 백준 1991 트리 순회
 21.08.24
 https://github.com/skyqnaqna/algorithm_study
 */

import Foundation

let n = Int(readLine()!)!
let A = Character("A").asciiValue!

// [0] : left, [1] : right
var tree = [[String]](repeating: [String](repeating: ".", count: 2), count: 26)

// A -> 0, B -> 1 ...
func atoi(_ s: String) -> Int {
  return Int(Character(s).asciiValue! - A)
}

for _ in 0 ..< n {
  let input = readLine()!.split(separator: " ").map { String($0) }

  if input[1] != "." {
    tree[atoi(input[0])][0] = input[1]
  }

  if input[2] != "." {
    tree[atoi(input[0])][1] = input[2]
  }
}

func preorder(_ root: String) {
  if root == "." {
    return
  }

  print(root, terminator: "")
  preorder(tree[atoi(root)][0])
  preorder(tree[atoi(root)][1])
}

func inorder(_ root: String) {
  if root == "." {
    return
  }

  inorder(tree[atoi(root)][0])
  print(root, terminator: "")
  inorder(tree[atoi(root)][1])
}

func postorder(_ root: String) {
  if root == "." {
    return
  }

  postorder(tree[atoi(root)][0])
  postorder(tree[atoi(root)][1])
  print(root, terminator: "")
}

preorder("A")
print()
inorder("A")
print()
postorder("A")