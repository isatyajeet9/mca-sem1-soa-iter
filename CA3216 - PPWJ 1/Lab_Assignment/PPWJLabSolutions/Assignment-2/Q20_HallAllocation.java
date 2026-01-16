public class Q20_HallAllocation {
    public static void main(String[] args) {
        int roll = 1027; 

        int lastDigit = roll % 10;

        if (lastDigit >= 0 && lastDigit <= 3) {
            System.out.println("Hall A");
        } else if (lastDigit >= 4 && lastDigit <= 6) {
            System.out.println("Hall B");
        } else if (lastDigit >= 7 && lastDigit <= 9) {
            System.out.println("Hall C");
        } else {
            System.out.println("Invalid roll number");
        }
    }
}
