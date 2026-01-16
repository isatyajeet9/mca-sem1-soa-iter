public class Q20_BinaryPattern {
    public static void main(String[] args) {
        System.out.println("Pattern:");
        int rows = 4; 
        
        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= i; j++) {

                int start;
                if (i % 2 == 0) { 
                    start = 0;
                } else { 
                    start = 1;
                }
                

                System.out.print((start + j + 1) % 2); 
            }
            System.out.println();
        }
    }
}