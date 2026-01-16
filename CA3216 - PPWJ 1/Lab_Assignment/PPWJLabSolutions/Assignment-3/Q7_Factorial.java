import java.util.Scanner;

public class Q7_Factorial {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        System.out.print("Enter a number to find its factorial: ");
        int num = obj.nextInt();

        long fact = 1; 
        if (num < 0) {
            System.out.println("Factorial is not defined for negative numbers.");
        } else {
            for (int i = 1; i <= num; i++) {
                fact *= i; 
            }
            System.out.println("Factorial of " + num + " is: " + fact);
        }
        obj.close();
    }
}