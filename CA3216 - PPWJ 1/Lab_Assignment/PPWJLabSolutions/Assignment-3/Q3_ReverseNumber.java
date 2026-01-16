import java.util.Scanner;

public class Q3_ReverseNumber {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        System.out.print("Enter a number to reverse: ");
        int num = obj.nextInt();
        
        int reversedNum = 0;
        int originalNum = num; 
        
    
        while (num != 0) {
            int digit = num % 10; 
            reversedNum = reversedNum * 10 + digit; 
            num /= 10; 
        }
        
        System.out.println("Original number: " + originalNum);
        System.out.println("Reversed number: " + reversedNum);
    }
}