import java.util.ArrayList;
import java.util.List;

public class TrafficLight {
    private final List<Lineable> queue = new ArrayList<>();

    public void add(Lineable vehicle) {
        if (vehicle.canPass()) {
            int insertIndex = 0;
            while (insertIndex < queue.size() && queue.get(insertIndex).canPass()) {
                insertIndex++;
            }
            queue.add(insertIndex, vehicle);
        } else {
            queue.add(vehicle);
        }
    }

    @Override
    public String toString() {
        if (queue.isEmpty()) {
            return "TrafficLight queue is empty";
        }

        StringBuilder builder = new StringBuilder("TrafficLight queue: [");
        for (int i = 0; i < queue.size(); i++) {
            builder.append(queue.get(i));
            if (i < queue.size() - 1) {
                builder.append(" -> ");
            }
        }
        builder.append("]");
        return builder.toString();
    }
}
