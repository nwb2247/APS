import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
    public static void main(String[] args) throws IOException {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	
    	int N = Integer.parseInt(br.readLine());
    	
    	double mul = Double.parseDouble(br.readLine());
    	double max = mul;
    	for (int i=1; i<N; i++) {
    		double cur = Double.parseDouble(br.readLine());
    		mul = Math.max(mul*cur, cur);
    		max = Math.max(max, mul);
    	}
    	System.out.println(String.format("%.3f", max));
    	
    	
    }
    

        
}