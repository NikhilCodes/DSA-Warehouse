/*
ALGORITHM : Selection Sort
WORST CASE => {
    PERFORMANCE:  O(n^2)
    SPACE:        O(1)
}
*/

import java.util.Arrays;

public class SelectionSort {
    public static void main(String[] args) {
        int[] arr;
        arr = new int[] {6,5,4,3,2,1};

        int l = arr.length;
        int minIndex, temp;
        for(int i=0;i<l;i++) {
            minIndex = l-1;
            for(int j=i;j<l;j++) {
                if(arr[minIndex] > arr[j]) {
                    minIndex = j;
                }
            }

            temp = arr[minIndex];
            arr[minIndex] = arr[i];
            arr[i] = temp;
        }
        System.out.print(Arrays.toString(arr));
    }
}
