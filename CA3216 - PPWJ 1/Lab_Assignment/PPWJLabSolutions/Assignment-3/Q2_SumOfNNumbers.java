import java.util.Scanner;

public class Q2_SumOfNNumbers {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        System.out.print("Enter a number (N): ");
        int n = obj.nextInt();
        
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            sum += i; 
        }
        
        System.out.println("The sum of first " + n + " natural numbers is: " + sum);
    
    }
}