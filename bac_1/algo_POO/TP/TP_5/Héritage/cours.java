package Héritage;

public class cours extends salle {
    boolean screen;
    boolean projecteur;

    public cours(int numéro, int capacité, String typeTableau, boolean screen, boolean projecteur) {
        super(numéro, capacité, typeTableau);
        this.screen = screen;
        this.projecteur = projecteur;
    }
    
    public cours() {
        super();
        this.screen = false;
        this.projecteur = false;
    }

    public boolean isScreen() {
        return this.screen;
    }
    public void setScreen(boolean screen) {
        this.screen = screen;
    }
    public boolean isProjecteur() {
        return this.projecteur;
    }
    public void setProjecteur(boolean projecteur) {
        this.projecteur = projecteur;
    }

    @Override
    public String toString() {
        return super.toString() + "\n"
            + "Ecran fixe : " + (screen ? "oui" :"non") + "\n"
            + "Rétroprojecteur fixe : " + (projecteur ? "oui" :"non") + "\n";

    }

    public static void main(String[] args) {
        System.out.println("=== Test de la classe cours ===\n");

        cours c1 = new cours(101, 30, "blanc", true, false);
        System.out.println("Objet c1 créé avec constructeur personnalisé :");
        System.out.println(c1);

        System.out.println("\nTest des getters hérités et spécifiques :");
        System.out.println("Numéro : " + c1.getNuméro());
        System.out.println("Capacité : " + c1.getCapacité());
        System.out.println("Type de tableau : " + c1.getTypeTableau());
        System.out.println("Écran : " + c1.isScreen());
        System.out.println("Projecteur : " + c1.isProjecteur());

        System.out.println("\nTest des setters hérités et spécifiques :");
        c1.setNuméro(202);
        c1.setCapacité(45);
        c1.setTypeTableau("vert");
        c1.setScreen(false);
        c1.setProjecteur(true);
        System.out.println(c1);

        System.out.println("\nTest du constructeur par défaut :");
        cours c2 = new cours();
        System.out.println(c2);

        System.out.println("\nModification de c2 via setters :");
        c2.setNuméro(303);
        c2.setCapacité(20);
        c2.setTypeTableau("noir");
        c2.setScreen(true);
        c2.setProjecteur(true);
        System.out.println(c2);

        System.out.println("\nNom de la classe via getNomClasse() : " + c2.getNomClasse());
    }
}
