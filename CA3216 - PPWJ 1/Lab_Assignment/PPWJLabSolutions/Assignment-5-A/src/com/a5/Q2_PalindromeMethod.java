package com.a5;

import java.util.Scanner;

class Q2_PalindromeMethod {
    static boolean isPalindrome(String s) {
        int i = 0, j = s.length() - 1;
        while (i < j) {
            if (s.charAt(i) != s.charAt(j))
                return false;
            i++;
            j--;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        System.out.print("Enter string: ");
        String s = obj.next();
        System.out.println(isPalindrome(s));
    }
}
