// a1q13
// Name: Satyajeet Nayak
// Question: Check if a year is leap year using logical operators

public class Q13_LeapYearCheck {
    public static void main(String[] args) {
        int year = 2004;
        if ((year % 4 == 0 && year % 100 != 0) || (year % 100 == 0 && year % 400 == 0))
            System.out.println(year + " is a Leap Year");
        else
            System.out.println(year + " is not a Leap Year");
    }
}
