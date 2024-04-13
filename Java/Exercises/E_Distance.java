public class E_Distance {
	double x;
	double y;
	
	public E_Distance(double x, double y) {
		this.x=x;
		this.y=y;
	}
		
	public double edistance(E_Distance other) {
		double part1 = Math.pow(x - other.x, 2);
	    double part2 = Math.pow(y - other.y, 2);
		return Math.sqrt(part1+ part2);
	}
	
    public static void main(String[] args) {
    	E_Distance p1= new E_Distance(0.2, 15);
    	E_Distance p2= new E_Distance(13.1, 11);
    	
    	double distance;
    	distance=p1.edistance(p2);
    	System.out.println(distance);
        }
    }



/**@author Luis Reindlmeier, Kevin Brot, Sarah Rochel**/
