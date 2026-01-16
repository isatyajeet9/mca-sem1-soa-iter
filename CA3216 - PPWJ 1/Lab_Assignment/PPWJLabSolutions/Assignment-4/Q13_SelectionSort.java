import java.util.Scanner;

class Q13_SelectionSort {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = obj.nextInt();
        int a[] = new int[n];

        System.out.println("Enter " + n + " integers:");
        for (int i = 0; i < n; i++)
            a[i] = obj.nextInt();

        for (int i = 0; i < n; i++) {
            int min = i;

            for (int j = i + 1; j < n; j++) {
                if (a[j] < a[min])
                    min = j;
            }

            int t = a[i];
            a[i] = a[min];
            a[min] = t;
        }

        for (int i = 0; i < n; i++)
            System.out.print(a[i] + " ");
    }
}
