/*
ALGORITHM : Selection Sort
WORST CASE => {
    PERFORMANCE:  O(n^2)
    SPACE:        O(1)
}
*/

fun main() {
    val arr = arrayOf(9, 8, 7, 6, 5, 4, 3, 2, 1)
    val l = arr.size - 1
    var minIndex:Int
    var tmp:Int
    for(i in 0..l) {
        minIndex = i
        for(j in i..l) {
            if(arr[minIndex] > arr[j]) {
                minIndex = j
            }
        }

        tmp = arr[minIndex]
        arr[minIndex] = arr[i]
        arr[i] = tmp
    }

    print("Sorted Array: ")
    println(arr.contentToString())
}