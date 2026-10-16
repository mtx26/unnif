import java.util.Arrays;
import java.util.Scanner;

public class MyBinaryInteger implements Comparable<MyBinaryInteger> {
    private final int value;

    public MyBinaryInteger(int value) {
        this.value = value;
    }

    @Override
    public int compareTo(MyBinaryInteger other) {
        return Integer.compare(Integer.bitCount(this.value), Integer.bitCount(other.value));
    }

    @Override
    public String toString() {
        return Integer.toBinaryString(value);
    }
    public static void tester() {
        Scanner Scanner = new Scanner(System.in);
        System.out.print("Donne un entier : ");
        int n = Scanner.nextInt();
        MyBinaryInteger[] tab = new MyBinaryInteger[n];
        for (int i = 0; i < n; i++) {
            System.out.print("Donne un entier : ");
            tab[i] = new MyBinaryInteger(Scanner.nextInt());     
        }
        Scanner.close();
        Arrays.sort(tab);
        System.out.println(Arrays.toString(tab));
    }
    public static void main(String[] args) {
        tester();
    }
}