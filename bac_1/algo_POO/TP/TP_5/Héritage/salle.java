package Héritage;

public class salle {
    int numéro;
    int capacité;
    String typeTableau;

    public salle(int numéro, int capacité, String typeTableau) {
        this.numéro = numéro;
        this.capacité = capacité;
        this.typeTableau = typeTableau;
    }
    public salle() {
        this.numéro = 0;
        this.capacité = 0;
        this.typeTableau = "blanc";
    }
    public String getNomClasse() {
        return getClass().getSimpleName();
    }
    public int getNuméro() {
        return this.numéro;
    }
    public void setNuméro(int numéro) {
        this.numéro = numéro;
    }
    public int getCapacité() {
        return this.capacité;
    }
    public void setCapacité(int capacité) {
        this.capacité = capacité;
    }
    public String getTypeTableau() {
        return this.typeTableau;
    }
    public void setTypeTableau(String typeTableau) {
        this.typeTableau = typeTableau;
    }
    @Override
    public String toString() {
        return "Type de salle : salle de " + getNomClasse() + "\n"
            + "Numéro : " + numéro + "\n"
            + "Capacité : " + capacité + "\n"
            + "Type de tableau : " + typeTableau;
    }
}
