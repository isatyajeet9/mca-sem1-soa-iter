import java.util.Scanner;

public class Q3_LeapYearMethod {

    static boolean isLeap(int year) {
        return (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter year: ");
        int y = sc.nextInt();
        System.out.println(isLeap(y) ? "Leap Year" : "Not a Leap Year");
    }
}
