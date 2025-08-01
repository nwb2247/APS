import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
    public static void main(String[] args) throws IOException {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st = new StringTokenizer(br.readLine());
    	
    	int sum = 0;
    	for (int i=0; i<5; i++) {
    		int j = Integer.parseInt(st.nextToken());
    		sum += j*j;
    	}
    	System.out.println(sum%10);
    	
    }
      
}