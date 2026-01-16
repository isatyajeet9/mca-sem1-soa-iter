import java.util.Scanner;

class Q20_ReplaceSubstring {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);

        System.out.print("Enter the main string: ");
        String s = obj.nextLine();
        System.out.print("Enter substring to replace: ");
        String old = obj.nextLine();
        System.out.print("Enter replacement substring: ");
        String nw = obj.nextLine();

        System.out.println(s.replace(old, nw));
    }
}
