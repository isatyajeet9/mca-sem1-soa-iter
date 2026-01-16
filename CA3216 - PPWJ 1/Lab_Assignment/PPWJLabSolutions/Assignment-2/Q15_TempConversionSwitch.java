public class Q15_TempConversionSwitch {
    public static void main(String[] args) {
        int choice = 1;       
        double Temp = 30.0;
        double OPTemp;
        String result = "";

        switch (choice) {
            case 1: // Celsius to Fahrenheit
                OPTemp = Temp * (9.0 / 5.0) + 32;
                result = Temp + "°C is " + OPTemp + "°F";
                break;
            case 2: // Fahrenheit to Celsius
                OPTemp = (Temp - 32) * (5.0 / 9.0);
                result = Temp + "°F is " + OPTemp + "°C";
                break;
            case 3: // Celsius to Kelvin
                OPTemp = Temp + 273.15;
                result = Temp + "°C is " + OPTemp + "K";
                break;
            default:
                result = "Invalid conversion choice.";
        }
        System.out.println(result);
    }
}
