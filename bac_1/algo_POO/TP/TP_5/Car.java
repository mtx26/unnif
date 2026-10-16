public class Car implements Lineable {
    private final String licensePlate;
    private final String brand;

    public Car(String licensePlate, String brand) {
        this.licensePlate = licensePlate;
        this.brand = brand;
    }

    @Override
    public boolean canPass() {
        return false;
    }

    @Override
    public String toString() {
        return "Car{licensePlate='" + licensePlate + "', brand='" + brand + "'}";
    }
}
