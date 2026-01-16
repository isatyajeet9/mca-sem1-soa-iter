public class Q11_HoursWithSuffix {
    public static void main(String[] args) {
        System.out.println("24 hours of the day with suffixes:");

        for (int hour = 0; hour < 24; hour++) {
            if (hour == 0) {
                System.out.println("12 Midnight (00:00)");
            } else if (hour < 12) {
                System.out.println(hour + " AM");
            } else if (hour == 12) {
                System.out.println("12 Noon (12:00)");
            } else {
                int pmHour = hour - 12;
                System.out.println(pmHour + " PM");
            }
        }
    }
}