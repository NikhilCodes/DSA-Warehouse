/*
ALGORITHM : Linear Search
WORST CASE => {
    PERFORMANCE:  O(n)
    SPACE:        O(1)
}
*/

import java.util.*

fun main() {
    print("Enter Element to search: ")
    val scanner = Scanner(System.`in`)
    val arr = arrayOf(5, 2, 7, 1, 8, 9, 4)

    val key:Int = scanner.nextInt()

    for(element in arr) {
        if (element == key) {
            println("Found!")
            return
        }
    }

    println("Not Found!")
}