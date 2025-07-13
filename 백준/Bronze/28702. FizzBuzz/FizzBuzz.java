import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int idx = 0;
    	int num = -1;
    	for (int i=0; i<3; i++) {
    		String s = br.readLine();
    		if (!s.equals("Fizz") && !s.equals("Buzz") && !s.equals("FizzBuzz")) {
    			idx = i;
    			num = Integer.parseInt(s);
    		}
    	}
    	
    	num += 3-idx;
    	String sol = "";
    	if (num%3 == 0) {
    		sol += "Fizz";
    	}
    	if (num%5 == 0) {
    		sol += "Buzz";
    	}
    	if (sol.equals("")) {
    		System.out.println(num);
    	} else {
    		System.out.println(sol);
    	}
    	
    	
    }
    
}