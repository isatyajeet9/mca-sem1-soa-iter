import java.util.Scanner;

class Q14_VowelConsonantCount {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String s = obj.nextLine().toLowerCase();

        int v = 0, c = 0;

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            if (ch >= 'a' && ch <= 'z') {
                if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
                    v++;
                else
                    c++;
            }
        }

        System.out.println("Vowels = " + v);
        System.out.println("Consonants = " + c);
    }
}
