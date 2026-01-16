import java.util.Scanner;

class Q5_LinearSearch {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = obj.nextInt();
        int a[] = new int[n];

        System.out.println("Enter " + n + " integers:");
        for (int i = 0; i < n; i++)
            a[i] = obj.nextInt();

        System.out.print("Enter key to search: ");
        int key = obj.nextInt();
        boolean found = false;

        for (int i = 0; i < n; i++) {
            if (a[i] == key) {
                found = true;
                break;
            }
        }

        System.out.println(found ? "Found" : "Not Found");
    }
}
