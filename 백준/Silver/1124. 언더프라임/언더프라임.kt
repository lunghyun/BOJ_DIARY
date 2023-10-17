fun isPrime(x: Int): Boolean {
    if (x < 2)
        return false
    for (i in 2 until x) {	// 2부터 x-1까지 반복
        if (x % i == 0) return false	// x가 한 번이라도 나누어 떨어지면 소수가 아님
    }
    return true	// 모두 반복해도 나누어 떨어지지 않으면 소수
}

fun main(args: Array<String>) {
    var (a, b) = readln().split(" ").map{it.toInt()}
    var output = 0
    for (i in a..b){
        var tmp = i
        var (div, cnt) = listOf(2, 0)
        while(tmp != 1){
            if (tmp % div == 0){
                tmp /= div
                cnt++
            }
            else
                div++
        }
        if (isPrime(cnt)){
            output++
        }
    }
    print(output)
}