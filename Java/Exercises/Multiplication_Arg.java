public class Multiplication_Arg {
    public static void main(String[] args) {

        int n = Integer.parseInt(args[0]);
        for (int i = 1; i <= 10; i++) {
            System.out.println(n + " x " + i + " = " + (n * i));
        }
    }
}
