```
import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
var count = 0
fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val st = StringTokenizer(readLine())
    val n = st.nextToken().toInt()
    val s = st.nextToken().toInt()
    with(StringTokenizer(readLine())){

            val list = mutableListOf<Int>()
            for(i in 0 until n){
                list.add(nextToken().toInt())
            }
            dfs(0,n,s,0,list)
            println(count)

    }

}

fun dfs(index : Int,n : Int, s:Int, result : Int , list : List<Int>){
    if(result == s && index != 0)
        count++
    if(index >= n)
        return
    for(i in index until n){
        dfs(i+1,n, s, result+list[i], list)
    }
}
```
