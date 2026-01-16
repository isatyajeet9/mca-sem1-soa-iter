public class Q3_SmallestOfFive {
    public static void main(String[] args) {
        int num1 = 15, num2 = 8, num3 = 22, num4 = 3, num5 = 12;

        int smallest = num1;

        if (num2 < smallest)
            smallest = num2;
        if (num3 < smallest)
            smallest = num3;
        if (num4 < smallest)
            smallest = num4;
        if (num5 < smallest)
            smallest = num5;

        System.out.println("Smallest number: " + smallest);
    }
}
