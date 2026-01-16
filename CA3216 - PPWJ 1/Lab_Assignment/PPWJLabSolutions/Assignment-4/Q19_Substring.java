import java.util.Scanner;

class Q19_Substring {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);

        System.out.print("Enter a string: ");
        String s = obj.nextLine();
        System.out.print("Enter start index: ");
        int start = obj.nextInt();
        System.out.print("Enter end index: ");
        int end = obj.nextInt();

        String sub = "";
        for (int i = start; i < end; i++)
            sub += s.charAt(i);

        System.out.println(sub);
    }
}
