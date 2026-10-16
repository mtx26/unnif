package TP.TP_6;

import java.util.ArrayList;
import java.util.List;

public class BiblioList extends Bibliotheque {
    private final List<Ouvrage> list = new ArrayList<>();

    @Override
    public boolean add(Ouvrage o) {
        if (o == null) return false;
        return list.add(o);
    }

    @Override
    public boolean delete(int cote) {
        return list.removeIf(o -> o.getCote() == cote);
    }

    @Override
    public Ouvrage findByCote(int cote) {
        for (Ouvrage o : list) if (o.getCote() == cote) return o;
        return null;
    }

    @Override
    public int size() {
        return list.size();
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Nombre d'ouvrages: ").append(size()).append('\n');
        for (Ouvrage o : list) sb.append(o).append('\n');
        return sb.toString();
    }
}
