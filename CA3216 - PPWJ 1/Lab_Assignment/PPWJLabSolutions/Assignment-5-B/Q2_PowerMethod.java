import java.util.Scanner;

public class Q2_PowerMethod {

    static double power(double a, double b) {
        return Math.pow(a, b);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a: ");
        double a = sc.nextDouble();
        System.out.print("Enter b: ");
        double b = sc.nextDouble();
        System.out.println("Result = " + power(a, b));
    }
}
