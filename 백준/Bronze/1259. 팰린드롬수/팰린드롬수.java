import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
    public static void main(String[] args) throws IOException {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringBuilder sb = new StringBuilder();
    	
    	String s = br.readLine();
    	while (!s.equals("0")) {
    		char[] chars = s.toCharArray();
    		boolean sol = true;
    		for (int i=0; i<=chars.length/2-1; i++) {
    			if (chars[i] != chars[chars.length-1-i]) {
    				sol = false;
    				break;
    			}
    		}
    		if (sol) {
    			sb.append("yes");
    		} else {
    			sb.append("no");
    		}
    		sb.append("\n");
    		s = br.readLine();
    	}
    	System.out.println(sb.toString());
    	
    }
      
}