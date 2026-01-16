class Q21_DiamondPattern {
    public static void main(String[] args) {
        int n = 5;

        for(int i = 1; i <= n; i += 2) {
            for(int s = 0; s < (n - i) / 2; s++) 
                System.out.print(" ");
            for(int j = 0; j < i; j++) 
                System.out.print("*");
            System.out.println();
        }

        for(int i = n - 2; i >= 1; i -= 2) {
            for(int s = 0; s < (n - i) / 2; s++) 
                System.out.print(" ");
            for(int j = 0; j < i; j++) 
                System.out.print("*");
            System.out.println();
        }
    }
}
