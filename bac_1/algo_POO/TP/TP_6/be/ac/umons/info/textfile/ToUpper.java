package TP.TP_6.be.ac.umons.info.textfile;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class ToUpper {

    public static void main(String[] args) {
        if (args.length != 2) {
            System.err.println("Usage: java be.ac.umons.info.textfile.ToUpper <input-file> <output-file>");
            System.exit(1);
        }

        Path inputPath = Path.of(args[0]);
        Path outputPath = Path.of(args[1]);

        try (BufferedReader reader = Files.newBufferedReader(inputPath);
             BufferedWriter writer = Files.newBufferedWriter(outputPath)) {

            String line;
            while ((line = reader.readLine()) != null) {
                writer.write(line.toUpperCase());
                writer.newLine();
            }

        } catch (IOException e) {
            System.err.println("Erreur lors du traitement des fichiers : " + e.getMessage());
            System.exit(2);
        }
    }
}
