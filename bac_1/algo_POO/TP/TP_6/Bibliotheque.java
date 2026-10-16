package TP.TP_6;

public abstract class Bibliotheque {
    public abstract boolean add(Ouvrage o);
    public abstract boolean delete(int cote);
    public abstract Ouvrage findByCote(int cote);
    public abstract int size();
    @Override
    public abstract String toString();
}
