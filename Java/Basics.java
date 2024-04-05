
public class Bascis {
	public static void main(String[] args) {
		
		int[] in= new int[3];
		in[0]=1;
		in[1]=2;
		in[2]=3;
		
		int[] j = {1,2,3};
		
		
		int x=5;
		boolean b=false;
		
		//if 
		if (b) {
			System.out.println("true");
		}
		
		else if(b) {
			System.out.println("true");
		}
		else {
			System.out.println("false");
		}
		
		//switch
		
		int grade=2;
		
		switch (grade) {
		
		case 1:
			System.out.println("very good");
			break;
		case 2:
			System.out.println("good");
			break;
		case 3:
			System.out.println("bad");
		case 4:
			System.out.println("very bad");
		default:
			System.out.println("dummy");
		}
		
		//for
		
		for (int i = 0; i<5; i++) {
			System.out.println(i);
			if (i==4) {
				continue;
			}
		}
		
		//for each
		int sum=0;
		for (int i : in) {
			sum++;
		}
		
		//while
		
		int i=0;
		while (i<5) {
			System.out.println(i);
			i++;
		}
		
		//do while
		
		do {
			System.out.println(i);
			i++;
		}
		while (i<5);
		
		
		
	}
}
