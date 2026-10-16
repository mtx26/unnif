package be.ac.umons.info.binaryfile;

import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;

public class SquaredTest {

    public static void main(String[] args) {
        if (args.length != 2) {
            System.err.println("Usage: java be.ac.umons.info.binaryfile.SquaredTest <file> <index>");
            System.exit(1);
        }

        Path filePath = Path.of(args[0]);
        int index;
        try {
            index = Integer.parseInt(args[1]);
        } catch (NumberFormatException e) {
            System.err.println("Le second argument doit être un entier.");
            System.exit(1);
            return;
        }

        if (index < 0 || index >= 1000) {
            System.err.println("L'index doit être compris entre 0 et 999.");
            System.exit(1);
        }

        if (!Files.exists(filePath)) {
            System.err.println("Fichier introuvable : " + filePath);
            System.exit(2);
        }

        try (FileChannel channel = FileChannel.open(filePath, StandardOpenOption.READ)) {
            long position = index * Integer.BYTES;
            if (channel.size() < position + Integer.BYTES) {
                System.err.println("Le fichier ne contient pas suffisamment de données.");
                System.exit(2);
            }

            ByteBuffer buffer = ByteBuffer.allocate(Integer.BYTES);
            channel.position(position);
            channel.read(buffer);
            buffer.flip();
            int value = buffer.getInt();
            int expected = index * index;
            System.out.println("Valeur lue à l'index " + index + " : " + value);
            System.out.println("Valeur attendue : " + expected);
            System.out.println(value == expected ? "Résultat : OK" : "Résultat : KO");
        } catch (IOException e) {
            System.err.println("Erreur de lecture du fichier binaire : " + e.getMessage());
            System.exit(2);
        }
    }
}
