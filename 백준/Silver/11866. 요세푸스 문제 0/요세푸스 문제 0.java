import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st;
    	StringBuilder sb = new StringBuilder();
    	
    	st = new StringTokenizer(br.readLine());
    	int N = Integer.parseInt(st.nextToken());
    	int K = Integer.parseInt(st.nextToken());
    	
    	ArrayDeque<Integer> q1 = new ArrayDeque<>();
    	for (int i=1; i<=N; i++) {
    		q1.addLast(i);
    	}
    	
    	sb.append("<");
    	while(!q1.isEmpty()) {
    		for (int i=1; i<=K-1; i++) {
    			q1.addLast(q1.pollFirst());
    		}
    		sb.append(q1.pollFirst()).append(", ");
    	}
    	sb.delete(sb.length()-2, sb.length());
    	sb.append(">");
    	System.out.println(sb.toString());
    	
    	
    	
    }
    
}