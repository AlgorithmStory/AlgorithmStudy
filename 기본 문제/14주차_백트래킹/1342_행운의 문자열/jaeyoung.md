```
import java.io.BufferedReader
import java.io.InputStreamReader

var hashMap = hashMapOf<Pair<Char,Int>,Boolean>()
fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val st = readLine()
    var result = dfs(st,st.length,"")
    val data = hashMapOf<Char,Int>()
    st.forEach {
        val count = data[it] ?:0
        data[it] = count+1
    }
    data.values.forEach {
        result/=getFactorial(it)
    }
    println(result)
}

fun getFactorial(n : Int) : Int{
     if(n == 1)
         return 1
     return getFactorial(n-1)*n
}

fun dfs(st : String , m : Int,data : String) : Int{
    var result = 0
    val dataSize = data.length
    if(dataSize == m){
        return 1
    }
    st.forEachIndexed { index, it ->
        val isVisit = hashMap[it to index] ?:false
        if(!isVisit){
            if(data.isEmpty() || data[dataSize-1] != it){
                hashMap[it to index] = true
                result += dfs(st,m,data+it)
                hashMap[it to index] = false
            } else
                return@forEachIndexed
        }
    }
    return result
}

```
