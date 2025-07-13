import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st;
    	StringBuilder sb = new StringBuilder();
    	
    	int N = Integer.parseInt(br.readLine());
    	HashMap<Integer, Integer> m = new HashMap<>();
    	st = new StringTokenizer(br.readLine());
    	for (int i=0 ; i<N; i++) {
    		int n = Integer.parseInt(st.nextToken());
    		if (!m.containsKey(n)) {
    			m.put(n, 1);
    		} else {
    			m.put(n, m.get(n)+1);
    		}
    	}
    	int M = Integer.parseInt(br.readLine());
    	st = new StringTokenizer(br.readLine());
    	for (int i=0; i<M; i++) {
    		int n = Integer.parseInt(st.nextToken());
    		if (m.get(n) == null) {
    			sb.append(0);
    		} else {
    			sb.append(m.get(n));
    		}
    		sb.append(" ");
    	}
    	System.out.println(sb.toString());
    	
    }
    
}