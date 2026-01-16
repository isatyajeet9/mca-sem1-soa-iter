import java.util.Scanner;

public class Q10_DecimalToBinary {

    static void binary(int n) {
        if (n == 0) return;
        binary(n / 2);
        System.out.print(n % 2);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number: ");
        int n = sc.nextInt();
        binary(n);
    }
}
