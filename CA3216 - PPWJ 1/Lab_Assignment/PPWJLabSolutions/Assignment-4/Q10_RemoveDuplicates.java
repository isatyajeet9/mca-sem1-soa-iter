import java.util.Scanner;

class Q10_RemoveDuplicates {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = obj.nextInt();
        int a[] = new int[n];

        System.out.println("Enter " + n + " integers:");
        for (int i = 0; i < n; i++)
            a[i] = obj.nextInt();

        for (int i = 0; i < n; i++) {
            boolean repeat = false;

            for (int j = 0; j < i; j++) {
                if (a[i] == a[j]) {
                    repeat = true;
                    break;
                }
            }

            if (!repeat)
                System.out.print(a[i] + " ");
        }
    }
}
