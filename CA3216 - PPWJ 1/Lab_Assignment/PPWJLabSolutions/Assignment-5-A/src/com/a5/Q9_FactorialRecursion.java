package com.a5;

import java.util.Scanner;

class Q9_FactorialRecursion {
    static int fact(int n) {
        if (n == 0)
            return 1;
        return n * fact(n - 1);
    }

    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        System.out.print("Enter number: ");
        int n = obj.nextInt();
        System.out.println(fact(n));
    }
}

