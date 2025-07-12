import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
    public static void main(String[] args) throws IOException {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st = new StringTokenizer(br.readLine());
    	
    	int A = Integer.parseInt(st.nextToken());
    	int B = Integer.parseInt(st.nextToken());
    	int N = Integer.parseInt(st.nextToken());
    	
    	int sol = 0;
    	int r = (N-A)/(A-B);
    	sol += r;
    	sol += (N-r*(A-B))/A;
    	if ((N-r*(A-B))%A != 0) sol++;
    	System.out.println(sol);
    }
      
}