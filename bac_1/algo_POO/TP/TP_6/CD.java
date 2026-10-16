package TP.TP_6;

public class CD extends Ouvrage {
    private String titre;
    private String auteur;

    public CD(String titre, String auteur, String dateEmprunt) {
        super(dateEmprunt);
        this.titre = titre;
        this.auteur = auteur;
    }

    public String getTitre() {
        return titre;
    }

    public void setTitre(String titre) {
        this.titre = titre;
    }

    public String getAuteur() {
        return auteur;
    }

    public void setAuteur(String auteur) {
        this.auteur = auteur;
    }

    @Override
    public String toString() {
        return "CD{" +
            "titre='" + titre + '\'' +
            ", auteur='" + auteur + '\'' +
            ", " + super.toString() +
            '}';
    }
}
