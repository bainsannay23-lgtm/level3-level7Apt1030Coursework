public class DroughtAdvisory {
    public static void printAdvisory(double rainfall, double temp) {
        if (rainfall < 200) {
            System.out.println("Irrigation Required");
        } else {
            if (temp > 30) {
                System.out.println("Monitor Soil");
            } else {
                System.out.println("Normal Conditions");
            }
        }
    }
    public static void main(String[] args) {
        printAdvisory(250, 32);
    }
}
