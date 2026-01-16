package com.a5;

class Q10_SortStrings {
    static String[] sortStrings(String arr[]) {
        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = 0; j < arr.length - i - 1; j++) {
                if (arr[j].compareTo(arr[j + 1]) > 0) {
                    String temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
        return arr;
    }

    public static void main(String[] args) {
        String arr[] = {"banana", "apple", "orange"};
        arr = sortStrings(arr);
        for (String s : arr)
            System.out.println(s);
    }
}
