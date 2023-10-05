fun main(args: Array<String>) {
    var n = readln().toInt()
    var arr = readln().split(' ').map{it.toDouble()}

    var max = 0
    for (i in 0 until n){
        var a: Double = -1000000000.0
        var temp = 0
        for(j in i+1 until n){
            var fa: Double = (arr[i]-arr[j])/(i-j)
            if(a < fa){
                a = fa
                temp += 1
            }
        }
        a = 1000000000.0
        for(j in i-1 downTo 0){
            var fa: Double = (arr[i]-arr[j])/(i-j)
            if(a > fa){
                a = fa
                temp += 1
            }
        }
        if(max < temp){
            max = temp
        }
    }
    print(max)
}