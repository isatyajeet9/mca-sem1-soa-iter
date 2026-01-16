import java.util.Scanner;

public class Q13_PowerCalculation {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter the base (x): ");
        int x = sc.nextInt();
        
        System.out.print("Enter the exponent (y): ");
        int y = sc.nextInt();
        
        long result = 1; 

        for (int i = 1; i <= y; i++) {
            result *= x; 
        }
        
        System.out.println(x + " raised to the power of " + y + " is: " + result);
    }
}