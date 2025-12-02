public class CircleCalc {
    public static void main(String[] args) {
        final double PI = 3.14159;
        double radius = 5.0;
        double area = PI * radius * radius;
        double circumference = 2 * PI * radius;
        
        System.out.printf("Radius: %.2f\n", radius);
        System.out.printf("Area: %.2f\n", area);
        System.out.printf("Circumference: %.2f\n", circumference);
    }
}
