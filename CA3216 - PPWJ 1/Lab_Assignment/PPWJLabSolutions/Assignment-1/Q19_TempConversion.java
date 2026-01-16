// a1q19
// Name: Satyajeet Nayak
// Question: Convert temperature from Celsius to Fahrenheit and vice versa

public class Q19_TempConversion {
    public static void main(String[] args) {
        float c = 25;
        float f = (c * 9 / 5) + 32;
        System.out.println("Celsius to Fahrenheit: " + f);
        float f2 = 77;
        float c2 = (f2 - 32) * 5 / 9;
        System.out.println("Fahrenheit to Celsius: " + c2);
    }
}
