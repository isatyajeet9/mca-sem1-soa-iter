import java.util.Scanner;

class Q11_ElementFrequency {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = obj.nextInt();
        int a[] = new int[n];

        System.out.println("Enter " + n + " integers:");
        for (int i = 0; i < n; i++)
            a[i] = obj.nextInt();

        for (int i = 0; i < n; i++) {
            if (a[i] == -1)
                continue;

            int count = 1;

            for (int j = i + 1; j < n; j++) {
                if (a[i] == a[j]) {
                    count++;
                    a[j] = -1;
                }
            }

            System.out.println(a[i] + " -> " + count);
        }
    }
}
