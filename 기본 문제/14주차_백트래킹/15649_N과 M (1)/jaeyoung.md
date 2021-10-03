```
import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.StringBuilder
import java.util.*
var n = 0
var m = 0
val arr by lazy {
    Array(m){0}
}
val visit by lazy {
    Array(n){false}
}
fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val st = StringTokenizer(readLine())
    n = st.nextToken().toInt()
    m = st.nextToken().toInt()
    dfs(n,m,0)
}

fun dfs(n : Int , m : Int, depth : Int){
    if(depth == m){
        val stringBuilder = StringBuilder()
        arr.forEach {
            stringBuilder.append("$it ")
        }
        println(stringBuilder.toString())
        return
    }
    for(i in 0 until n){
        if(!visit[i]){
            visit[i] = true
            arr[depth] = i + 1
            dfs(n, m, depth+1)
            visit[i] = false
        }

    }
}
```
