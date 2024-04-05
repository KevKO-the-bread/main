import java.util.Scanner;

public class Multiplication_2 {
    public static void main(String[] args) {

    	int message_int;
    	
    	Scanner scan = new Scanner(System.in);
    	System.out.println("Enter a line of text:");
    	message_int = scan.nextInt();
    	
    	
        for (int i = 1; i <= 10; i++) {
            System.out.println(message_int + " x " + i + " = " + (message_int * i));
        }
    }
}

/**@author Luis Reindlmeier, Kevin Brot, Sarah Rochel**/

