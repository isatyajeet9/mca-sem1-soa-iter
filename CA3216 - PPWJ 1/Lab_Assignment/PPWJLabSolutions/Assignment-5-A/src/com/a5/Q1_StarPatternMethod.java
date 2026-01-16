package com.a5;

import java.util.Scanner;

class Q1_StarPatternMethod {
    static void printPattern(int rows) {
        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }

    public static void main(String args[]) {
        Scanner obj = new Scanner(System.in);
        System.out.print("Enter number of rows: ");
        int r = obj.nextInt();
        printPattern(r);
    }
}
