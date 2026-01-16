// a1q17
// Name: Satyajeet Nayak
// Question: Calculate sum of digits of a number using operators

public class Q17_SumOfDigits {
    public static void main(String[] args) {
        int number = 1234;
        
        int digit1 = number / 1000;           // 1
        int digit2 = (number / 100) % 10;     // 2
        int digit3 = (number / 10) % 10;      // 3
        int digit4 = number % 10;             // 4
        
        int sum = digit1 + digit2 + digit3 + digit4;       

        System.out.println("Sum of Digits: " + sum);
    }
}