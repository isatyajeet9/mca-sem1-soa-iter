package com.a5;

import java.util.Scanner;

class Q7_CheckMultiple {
    static boolean isMultiple(int a, int b) {
        if (a % b == 0 || b % a == 0)
            return true;
        return false;
    }

    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        System.out.print("Enter two numbers: ");
        int a = obj.nextInt();
        int b = obj.nextInt();
        System.out.println(isMultiple(a, b));
    }
}