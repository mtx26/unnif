package TP.TP_6;

public class Main {
    public static void main(String[] args) {
        System.out.println("-- Test BiblioTab (tableau) --");
        Bibliotheque btab = new BiblioTab();
        testBibliotheque(btab);

        System.out.println("\n-- Test BiblioList (ArrayList) --");
        Bibliotheque blist = new BiblioList();
        testBibliotheque(blist);
    }

    private static void testBibliotheque(Bibliotheque b) {
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
