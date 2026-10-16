package TP.TP_6;

public class Livre extends Ouvrage {
    private String auteur;
    private String titre;
    private String editeur;

    public Livre(String auteur, String titre, String editeur, String dateEmprunt) {
        super(dateEmprunt);
        this.auteur = auteur;
        this.titre = titre;
        this.editeur = editeur;
    }

    public String getAuteur() {
        return auteur;
    }

    public void setAuteur(String auteur) {
        this.auteur = auteur;
    }

    public String getTitre() {
        return titre;
    }

    public void setTitre(String titre) {
        this.titre = titre;
    }

    public String getEditeur() {
        return editeur;
    }

    public void setEditeur(String editeur) {
        this.editeur = editeur;
    }

    @Override
    public String toString() {
        return "Livre{" +
            "auteur='" + auteur + '\'' +
            ", titre='" + titre + '\'' +
            ", editeur='" + editeur + '\'' +
            ", " + super.toString() +
            '}';
    }
}
