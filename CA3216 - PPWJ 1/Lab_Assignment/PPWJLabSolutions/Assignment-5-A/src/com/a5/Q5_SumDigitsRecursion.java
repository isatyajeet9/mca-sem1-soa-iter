package com.a5;

import java.util.Scanner;

class Q5_SumDigitsRecursion {
    static int sumDigits(int n) {
        if (n == 0)
            return 0;
        return (n % 10) + sumDigits(n / 10);
    }

    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        System.out.print("Enter number: ");
        int n = obj.nextInt();
        System.out.println(sumDigits(n));
    }
}
