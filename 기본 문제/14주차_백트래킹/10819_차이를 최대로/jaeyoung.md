```
import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.math.abs

var max = 0

fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val n = readLine().toInt()
    val st = StringTokenizer(readLine())
    val list = mutableListOf<Int>()
    for(i in 0 until n){
        list.add(st.nextToken().toInt())
    }
    dfs(n,list,0, Array(n){false},Array(n){0})
    println(max)
}

fun dfs(n : Int,dataList : List<Int> , depth : Int , visit : Array<Boolean>, tempArray : Array<Int>){
    if(depth == n){
        tempArray.checkResult()
    }
    dataList.forEachIndexed { index, i ->
        if(!visit[index]){
            visit[index] = true
            tempArray[depth] = i
            dfs(n,dataList, depth + 1,visit, tempArray)
            visit[index] = false
        }
    }

}

fun Array<Int>.checkResult() {
    var result = 0
    for(i in 2..size){
        result+= abs(this[i-2]-this[i-1])
    }
    max = max.coerceAtLeast(result)
}
```
