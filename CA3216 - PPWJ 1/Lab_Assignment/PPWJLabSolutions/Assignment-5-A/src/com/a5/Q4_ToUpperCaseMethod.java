package com.a5;

import java.util.Scanner;

class Q4_ToUpperCaseMethod {
    static void toUpper(char[] arr) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] >= 'a' && arr[i] <= 'z')
                arr[i] = (char)(arr[i] - 32);
        }
    }

    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        System.out.print("Enter string: ");
        String s = obj.next();
        char[] ch = s.toCharArray();
        toUpper(ch);
        System.out.println(ch);
    }
}
