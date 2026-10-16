package Héritage;

public class informatique extends salle {
    int poste;
    String typePoste;

    public informatique(int numéro, int capacité, String typeTableau, int poste, String typePoste) {
        super(numéro, capacité, typeTableau);
        this.poste = poste;
        this.typePoste = typePoste;
    }
    public informatique() {
        super();
        this.poste = 0;
        this.typePoste = "terminaux X";
    }
    public int getPoste() {
        return this.poste;
    }
    public void setPoste(int poste) {
        this.poste = poste;
    }
    public String getTypePoste() {
        return this.typePoste;
    }
    public void setTypePoste(String typePoste) {
        this.typePoste = typePoste;
    }
    @Override
    public String toString() {
        return super.toString() + "\n"
            + "Nombre de postes : " + poste + "\n"
            + "Type de postes : " + typePoste + "\n";

    }
}
