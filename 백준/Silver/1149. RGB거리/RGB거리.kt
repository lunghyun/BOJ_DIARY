import java.lang.Integer.min

fun main(args: Array<String>) {
    var n = readln().toInt()
    var arr = mutableListOf(mutableListOf(0, 0, 0))
    for (i in 1 .. n) {
        arr.add(readln().split(" ").map{it.toInt()}.toMutableList())
    }
    for(i in 1..n){
        arr[i][0] += min(arr[i-1][1], arr[i-1][2])
        arr[i][1] += min(arr[i-1][0], arr[i-1][2])
        arr[i][2] += min(arr[i-1][0], arr[i-1][1])
    }
    print(minOf(arr[n][0], arr[n][1], arr[n][2]))
}