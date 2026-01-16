import java.util.Scanner;

public class Q19_PerfectNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number to check if it's perfect: ");
        int num = sc.nextInt();
        
        int sumOfDivisors = 0;
        
        for (int i = 1; i < num; i++) {
            if (num % i == 0) {
                sumOfDivisors += i;
            }
        }
        
        if (sumOfDivisors == num && num > 0) {
            System.out.println(num + " is a perfect number.");
        } else {
            System.out.println(num + " is not a perfect number.");
        }
    }
}