public class Q19_ArmstrongNumber {
    public static void main(String[] args) {
        int num = 153;
        int Org = num;
        int sum = 0;

        while (num > 0) {
            int digit = num % 10;
            sum += digit * digit * digit;
            num /= 10;
        }

        if (sum == Org)
            System.out.println(Org + " is an Armstrong number.");
        else
            System.out.println(Org + " is not an Armstrong number.");
    }
}
