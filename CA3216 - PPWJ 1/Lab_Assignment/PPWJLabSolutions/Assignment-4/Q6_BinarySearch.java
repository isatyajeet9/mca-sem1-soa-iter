import java.util.Scanner;

class Q6_BinarySearch {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = obj.nextInt();
        int a[] = new int[n];

        System.out.println("Enter " + n + " integers in sorted order:");
        for (int i = 0; i < n; i++)
            a[i] = obj.nextInt();
        System.out.print("Enter key to search: ");
        int key = obj.nextInt();

        int low = 0, high = n - 1;
        boolean found = false;

        while (low <= high) {
            int mid = (low + high) / 2;

            if (a[mid] == key) {
                found = true;
                break;
            } else if (key < a[mid])
                high = mid - 1;
            else
                low = mid + 1;
        }

        System.out.println(found ? "Found" : "Not Found");
    }
}
