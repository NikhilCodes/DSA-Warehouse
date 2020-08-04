/*
ALGORITHM : Insertion Sort
WORST CASE => {
    PERFORMANCE:  O(n^2)
    SPACE:        O(1)
}
*/

fun main() {
    val arr = arrayOf(9, 8, 7, 6, 5, 4, 3, 2, 1)

    val l = arr.size

    var tmp:Int
    for(i in 1..l) {
        for(j in i downTo 1) {
            if(arr[j] < arr[j-1]) {
                tmp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = tmp
            }
        }
    }

    print("Sorted Array: ")
    println(arr.contentToString())
}