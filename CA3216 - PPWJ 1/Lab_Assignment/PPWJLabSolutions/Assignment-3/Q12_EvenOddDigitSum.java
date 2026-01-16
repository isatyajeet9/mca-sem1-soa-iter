import java.util.Scanner;

public class Q12_EvenOddDigitSum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = sc.nextInt();
        
        int evenSum = 0;
        int oddSum = 0;
        int originalNum = num;
        
        while (num != 0) {
            int digit = num % 10;
            
            if (digit % 2 == 0) {
                evenSum += digit; 
                oddSum += digit; 
            }
            
            num /= 10; 
        }
        
        System.out.println("For the number " + originalNum + ":");
        System.out.println("Sum of even digits: " + evenSum);
        System.out.println("Sum of odd digits: " + oddSum);
    }
}