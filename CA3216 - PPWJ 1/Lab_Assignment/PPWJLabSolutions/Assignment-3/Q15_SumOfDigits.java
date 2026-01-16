import java.util.Scanner;

public class Q15_SumOfDigits {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number to find the sum of its digits: ");
        int num = sc.nextInt();
        
        int sum = 0;
        int originalNum = num;
        
        while (num != 0) {
            int digit = num % 10; 
            sum += digit; 
            num /= 10;
        }
        
        System.out.println("The sum of digits in " + originalNum + " is: " + sum);
    }
}