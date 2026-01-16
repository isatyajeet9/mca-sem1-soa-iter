package com.a5;

import java.util.Scanner;

class Q3_ReverseStringMethod {
    static String revString(String s) {
        String rev = "";
        for (int i = s.length() - 1; i >= 0; i--) {
            rev = rev + s.charAt(i);
        }
        return rev;
    }

    public static void main(String args[]) {
        Scanner obj = new Scanner(System.in);
        System.out.print("Enter string: ");
        String s = obj.next();
        
        System.out.println(revString(s));
    }
}
