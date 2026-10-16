package be.ac.umons.info.textfile;

import java.io.BufferedReader;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class FrequencyAnalyser {

    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("Usage: java be.ac.umons.info.textfile.FrequencyAnalyser <input-file>");
            System.exit(1);
        }

        Path inputPath = Path.of(args[0]);
        int[] counts = new int[128];
        int totalLetters = 0;

        try (BufferedReader reader = Files.newBufferedReader(inputPath, StandardCharsets.UTF_8)) {
            String line;
            while ((line = reader.readLine()) != null) {
                for (char c : line.toCharArray()) {
                    if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z')) {
                        counts[c]++;
                        totalLetters++;
                    }
                }
            }
        } catch (IOException e) {
            System.err.println("Erreur de lecture du fichier : " + e.getMessage());
            System.exit(2);
        }

        List<LetterFrequency> frequencies = new ArrayList<>();
        for (char c = 'A'; c <= 'Z'; c++) {
            frequencies.add(new LetterFrequency(c, counts[c]));
        }
        for (char c = 'a'; c <= 'z'; c++) {
            frequencies.add(new LetterFrequency(c, counts[c]));
        }

        frequencies.sort(Comparator
            .comparingInt(LetterFrequency::getCount).reversed()
            .thenComparing(LetterFrequency::getCharacter));

        System.out.println("Fréquences des lettres dans " + inputPath.getFileName() + " :");
        if (totalLetters == 0) {
            System.out.println("Aucune lettre trouvée dans le fichier.");
            return;
        }

        for (LetterFrequency entry : frequencies) {
            double percentage = entry.getCount() * 100.0 / totalLetters;
            System.out.printf("%c (%d) : %d %.2f%%%n", entry.getCharacter(), (int) entry.getCharacter(), entry.getCount(), percentage);
        }
    }

    private static class LetterFrequency {
        private final char character;
        private final int count;

        private LetterFrequency(char character, int count) {
            this.character = character;
            this.count = count;
        }

        public char getCharacter() {
            return character;
        }

        public int getCount() {
            return count;
        }
    }
}
