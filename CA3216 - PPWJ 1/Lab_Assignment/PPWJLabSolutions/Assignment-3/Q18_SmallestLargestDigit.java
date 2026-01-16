import java.util.Scanner;

public class Q18_SmallestLargestDigit {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = sc.nextInt();
        
        if (num == 0) {
            System.out.println("Smallest digit: 0, Largest digit: 0");
        }

        int smallest = 9; 
        int largest = 0;  
        int originalNum = num;
        
        while (num != 0) {
            int digit = num % 10;
            
            if (digit > largest) {
                largest = digit;
            }
            if (digit < smallest) {
                smallest = digit;
            }
            
            num /= 10;
        }
        
        System.out.println("In the number " + originalNum + ":");
        System.out.println("Smallest digit is: " + smallest);
        System.out.println("Largest digit is: " + largest);
    }
}