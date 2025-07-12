import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
    public static void main(String[] args) throws IOException {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st;
    	StringBuilder sb = new StringBuilder();
    	
    	int T = Integer.parseInt(br.readLine());
    	for (int t=0; t<T; t++) {
    		st = new StringTokenizer(br.readLine());
    		int H = Integer.parseInt(st.nextToken());
    		int W = Integer.parseInt(st.nextToken());
    		int N = Integer.parseInt(st.nextToken());
    		int x = (N-1)%H + 1;
    		int y = (N-1)/H + 1;
    		sb.append(x + String.format("%02d", y)).append("\n");
    	}
    	System.out.println(sb.toString());
    	
    }
      
}