import java.util.Scanner;

class Q15_ReverseString {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);

        System.out.print("Enter a string: ");
        String s = obj.nextLine();
        String rev = "";

        for (int i = s.length() - 1; i >= 0; i--)
            rev += s.charAt(i);

        System.out.println(rev);
    }
}
