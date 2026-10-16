package be.ac.umons.info.binaryfile;

import java.io.DataOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class Squared {

    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("Usage: java be.ac.umons.info.binaryfile.Squared <output-file>");
            System.exit(1);
        }

        Path outputPath = Path.of(args[0]);

        try (DataOutputStream output = new DataOutputStream(Files.newOutputStream(outputPath))) {
            for (int i = 0; i < 1000; i++) {
                output.writeInt(i * i);
            }
        } catch (IOException e) {
            System.err.println("Erreur lors de l'écriture du fichier binaire : " + e.getMessage());
            System.exit(2);
        }
    }
}
