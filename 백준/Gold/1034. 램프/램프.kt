import java.util.*

fun main() {
    val (n, m) = readln().split(" ").map { it.toInt() }
    val lamp = Array(n) { readln() }
    val k = readln().toInt()

    var maxOn = 0

    for (i in 0 until n) {
        val offCount = lamp[i].count { it == '0' }
        if (offCount <= k && (k - offCount) % 2 == 0) {
            maxOn = maxOf(maxOn, lamp.count { it == lamp[i] })
        }
    }

    println(maxOn)
}
