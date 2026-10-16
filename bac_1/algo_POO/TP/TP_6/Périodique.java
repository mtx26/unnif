package TP.TP_6;

public class Périodique extends Ouvrage {
    private String nom;
    private int numero;
    private String periodicite;

    public Périodique(String nom, int numero, String periodicite, String dateEmprunt) {
        super(dateEmprunt);
        this.nom = nom;
        this.numero = numero;
        this.periodicite = periodicite;
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public String getPeriodicite() {
        return periodicite;
    }

    public void setPeriodicite(String periodicite) {
        this.periodicite = periodicite;
    }

    @Override
    public String toString() {
        return "Périodique{" +
            "nom='" + nom + '\'' +
            ", numero=" + numero +
            ", periodicite='" + periodicite + '\'' +
            ", " + super.toString() +
            '}';
    }
}