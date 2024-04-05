
public class CharAnalyzer {
	    String word;
	    char letter;

	    public CharAnalyzer(String word, char letter) {
	        this.word = word;
	        this.letter = letter;
	    }

	    public int analyze() {
	        int count = 0;
	        for (int i = 0; i < word.length(); i++) {
	            if (word.charAt(i) == letter) {
	                count++;
	            }
	        }
	        return count;
	    }

	    public void print() {
	        int count = analyze();
	        System.out.println("The char '" + letter + "' is " + count + " times in " + word +".");
	    }

	    public static void main(String[] args) {
	        String text = "Hello, wooorld!";
	        char ch = 'o';
	       
	        CharAnalyzer analyzer = new CharAnalyzer(text, ch);
	        analyzer.print(); 
	    }
	}
/**@author Luis Reindlmeier, Kevin Brot, Sarah Rochel**/
