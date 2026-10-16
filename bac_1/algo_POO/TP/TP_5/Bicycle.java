public class Bicycle implements Lineable {
    private final String color;
    private final String brand;

    public Bicycle(String color, String brand) {
        this.color = color;
        this.brand = brand;
    }

    @Override
    public boolean canPass() {
        return true;
    }

    @Override
    public String toString() {
        return "Bicycle{color='" + color + "', brand='" + brand + "'}";
    }
}
