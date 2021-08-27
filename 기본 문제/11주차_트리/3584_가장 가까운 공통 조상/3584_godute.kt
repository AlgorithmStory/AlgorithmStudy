import java.util.*
import kotlin.collections.ArrayList

data class Node(
    var number: Int = 0,
    var parent: Int = 0,
    var childList: MutableList<Int> = mutableListOf()
)

/*
트리를 부모 방향으로 순회하며, 부모 리스트를 채우는 함수
nodeList : 전체 tree 정보 담긴 ArrayList
parentList : 부모 노드 List
node : 현재 node
 */
fun recursiveSearch(nodeList:ArrayList<Node>, parentList: MutableList<Int>, node: Int) {
    if(nodeList[node].parent == 0) { // root인 경우
        return
    }

    val parent = nodeList[node].parent
    parentList.add(parent)
    recursiveSearch(nodeList, parentList, parent)
}

/*
solution 함수
nodeList : 전체 tree 정보를 담은 ArrayList
firstNode : 가장 가까운 공통 조상을 구할 노드 중 첫번째
secondNode : 가장 가까운 공통 조상을 구할 노드 중 두번째
return : 두 노드의 조상의 교집합중 첫번째
 */
fun solution(nodeList: ArrayList<Node>, firstNode: Int, secondNode: Int): Int {
    var firstParentList = mutableListOf<Int>(firstNode)
    var secondParentList = mutableListOf<Int>(secondNode)

    recursiveSearch(nodeList, firstParentList, firstNode)
    recursiveSearch(nodeList, secondParentList, secondNode)

    return firstParentList.intersect(secondParentList).first()
}

fun main() {
    val reader = Scanner(System.`in`)
    val testCase = reader.nextInt()

    for (t in 1..testCase) {
        val nodeCount = reader.nextInt()
        var nodeList = ArrayList<Node>(nodeCount)

        for (i in 0..nodeCount) {
            nodeList.add(Node())
        }

        for (i in 1 until nodeCount) {
            val parent = reader.nextInt()
            val child = reader.nextInt()

            // 부모 인덱스에 자식리스트 추가 (자식은 여러명)
            // 자식 인덱스에 부모 설정 (부모는 하나)
            nodeList[parent].childList.add(child)
            nodeList[child].parent = parent
        }

        val firstNode = reader.nextInt()
        val secondNode = reader.nextInt()

        println(solution(nodeList, firstNode, secondNode))
    }
}