/*
ALGORITHM : Insertion Sort
WORST CASE => {
    PERFORMANCE:  O(n^2)
    SPACE:        O(1)
}
*/

import java.util.Arrays;

public class InsertionSort {
    public static void main(String[] args)  {
        int[] arr;
        arr = new int[] {6, 5, 4, 3, 2, 1};

        int l = arr.length;
        int temp;
        for(int i=1;i<l;i++) {
            for(int j=i;j>0;j--) {
                if (arr[j-1] > arr[j]) {
                    temp = arr[j-1];
                    arr[j-1] = arr[j];
                    arr[j] = temp;
                }
            }
        }

        System.out.println(Arrays.toString(arr));
    }
}
