// a1q16
// Name: Satyajeet Nayak
// Question: Calculate final price after discount

public class Q16_DiscountCalculation {
    public static void main(String[] args) {
        float price = 500, discount = 10;
        float finalPrice = price - (price * discount / 100);
        System.out.println("Final Price is: " + finalPrice);
    }
}
