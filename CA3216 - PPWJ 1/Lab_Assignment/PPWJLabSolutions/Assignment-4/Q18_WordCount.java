import java.util.Scanner;

class Q18_WordCount {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);

        System.out.print("Enter a string to count words: ");
        String s = obj.nextLine().trim();
        String words[] = s.split("\\s+");

        System.out.println("Word Count = " + words.length);
    }
}
