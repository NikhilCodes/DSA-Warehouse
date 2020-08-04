/*
ALGORITHM : Linear Search
WORST CASE => {
    PERFORMANCE:  O(n)
    SPACE:        O(1)
}
*/

import java.util.Scanner;

public class LinearSearch {
    public static void  main(String[] args) {
        Scanner myObj = new Scanner(System.in);

        int[] arr;
        arr = new int[] {3, 8, 1, 7, 5, 9, 2};

        System.out.print("Enter Element to find: ");
        int key = myObj.nextInt();
        for (int element : arr) {
            if (element == key) {
                System.out.println("Found!");
                return;
            }
        }
        System.out.println("Not Found!");
    }
}
