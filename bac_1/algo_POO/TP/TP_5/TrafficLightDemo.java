public class TrafficLightDemo {
    public static void main(String[] args) {
        TrafficLight trafficLight = new TrafficLight();

        trafficLight.add(new Car("ABC-123", "Peugeot"));
        trafficLight.add(new Bicycle("Rouge", "Decathlon"));
        trafficLight.add(new Car("XYZ-999", "Toyota"));
        trafficLight.add(new Bicycle("Bleu", "Trek"));
        trafficLight.add(new Car("DEF-456", "Renault"));

        System.out.println(trafficLight);
    }
}
