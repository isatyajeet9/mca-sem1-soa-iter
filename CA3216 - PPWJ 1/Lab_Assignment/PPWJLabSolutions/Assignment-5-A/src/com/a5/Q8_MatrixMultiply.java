package com.a5;

class Q8_MatrixMultiply {

    static int[][] multiply(int a[][], int b[][]) {
        int r1 = a.length;
        int c1 = a[0].length;
        int c2 = b[0].length;

        int c[][] = new int[r1][c2];

        for (int i = 0; i < r1; i++)
            for (int j = 0; j < c2; j++)
                for (int k = 0; k < c1; k++)
                    c[i][j] += a[i][k] * b[k][j];

        return c;
    }

    public static void main(String[] args) {
        int a[][] = {{1, 6}, {3, 4}};
        int b[][] = {{2, 5}, {4, 5}};

        int c[][] = multiply(a, b);

        for (int i = 0; i < c.length; i++) {
            for (int j = 0; j < c[0].length; j++) {
                System.out.print(c[i][j] + " ");
            }
            System.out.println();
        }
    }
}