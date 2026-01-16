import java.util.Scanner;

class Q17_SortCharacters {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);

        String s = obj.nextLine();
        char a[] = s.toCharArray();

        for (int i = 0; i < a.length - 1; i++) {
            for (int j = 0; j < a.length - 1 - i; j++) {
                if (a[j] > a[j + 1]) {
                    char t = a[j];
                    a[j] = a[j + 1];
                    a[j + 1] = t;
                }
            }
        }

        System.out.println(new String(a));
    }
}
