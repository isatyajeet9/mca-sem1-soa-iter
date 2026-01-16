import java.util.Scanner;

public class Q8_PrimeFactors {

    static void primeFactors(int n, int i) {
        if (n == 1) return;
        if (n % i == 0) {
            System.out.print(i + " ");
            primeFactors(n / i, i);
        } else {
            primeFactors(n, i + 1);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number: ");
        int n = sc.nextInt();
        primeFactors(n, 2);
    }
}
