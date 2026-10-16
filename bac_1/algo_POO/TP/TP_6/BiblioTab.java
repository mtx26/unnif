package TP.TP_6;

public class BiblioTab extends Bibliotheque {
    final int max = 50;
    private Ouvrage[] tab = new Ouvrage[max];
    private int n = 0;

    public boolean add(Ouvrage o) {
        if (n < max) {
            tab[n++] = o;
            return true;
        }
        return false;
    }
    public boolean delete(int cote) {
        for (int i = 0; i < n; i++) {
            if (tab[i] != null && tab[i].getCote() == cote) {
                // shift left
                for (int j = i; j < n - 1; j++) tab[j] = tab[j + 1];
                tab[n - 1] = null;
                n--;
                return true;
            }
        }
        return false;
    }

    public Ouvrage findByCote(int cote) {
        for (int i = 0; i < n; i++) {
            if (tab[i] != null && tab[i].getCote() == cote) return tab[i];
        }
        return null;
    }

    public int size() {
        return n;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(tab[i]).append("\n");
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        BiblioTab b = new BiblioTab();
        Livre l = new Livre("Victor Hugo", "Les Misérables", "Gallimard", null);
        CD cd = new CD("The Wall", "Pink Floyd", "2026-06-02");
        Périodique p = new Périodique("Science", 42, "mensuel", null);

        b.add(l);
        b.add(cd);
        b.add(p);

        System.out.println("Après ajout:");
        System.out.println(b);

        int coteASupprimer = l.getCote();
        System.out.println("Suppression cote " + coteASupprimer + " -> " + b.delete(coteASupprimer));

        System.out.println("Après suppression:");
        System.out.println(b);
    }

}
