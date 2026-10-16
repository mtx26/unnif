package TP.TP_6;

public abstract class Ouvrage {
    private static int compteur = 0;
    private String dateEmprunt;
    private final int cote;

    public Ouvrage(String dateEmprunt) {
        this.dateEmprunt = dateEmprunt;
        this.cote = ++compteur;
    }

    public String getDateEmprunt() {
        return dateEmprunt;
    }

    public void setDateEmprunt(String dateEmprunt) {
        this.dateEmprunt = dateEmprunt;
    }

    public int getCote() {
        return cote;
    }

    @Override
    public String toString() {
        return "cote=" + cote + ", dateEmprunt=" + (dateEmprunt == null ? "aucune" : dateEmprunt);
    }
}
