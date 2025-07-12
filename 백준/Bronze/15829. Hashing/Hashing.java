import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
    public static void main(String[] args) throws IOException {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	
    	int L = Integer.parseInt(br.readLine());
    	char[] chars = br.readLine().toCharArray();
    	Long sol = 0L;
    	long r = 1L;
    	long m = 1234567891L;
    	for (int i=0; i<L; i++) {
    		sol += ((long) chars[i]-'a'+1) * r;
    		sol %= m;
    		r = (r*31)%m;
    	}
    	System.out.println(sol);
    	
    }
      
}