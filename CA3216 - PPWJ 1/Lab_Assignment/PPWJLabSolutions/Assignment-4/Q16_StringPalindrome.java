import java.util.Scanner;

class Q16_StringPalindrome {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);

        System.out.print("Enter a string to check for palindrome: ");
        String s = obj.nextLine();
        String rev = "";

        for (int i = s.length() - 1; i >= 0; i--)
            rev += s.charAt(i);

        if (s.equals(rev))
            System.out.println("Palindrome");
        else
            System.out.println("Not Palindrome");
    }
}
