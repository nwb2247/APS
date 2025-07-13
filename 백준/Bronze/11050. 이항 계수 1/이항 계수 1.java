import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int[][] comb = new int[11][11];
	
	static {
		for (int i=1; i<=10; i++) {
			comb[i][0] = 1;
			comb[i][i] = 1;
		}
		for (int i=2; i<=10; i++) {
			for (int j=1; j<i; j++) {
				comb[i][j] = comb[i-1][j-1]+comb[i-1][j];
			}
		}
	}
	
    public static void main(String[] args) throws IOException {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st = new StringTokenizer(br.readLine());
    	
    	System.out.println(comb[Integer.parseInt(st.nextToken())][Integer.parseInt(st.nextToken())]);	
    	
    }
      
}
