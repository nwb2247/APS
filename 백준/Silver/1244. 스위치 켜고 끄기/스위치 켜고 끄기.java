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
    	
    	int N = Integer.parseInt(br.readLine());
    	boolean[] arr = new boolean[N+1];
    	st = new StringTokenizer(br.readLine());
    	for (int i=1; i<=N; i++) {
    		if (Integer.parseInt(st.nextToken()) == 1) {
    			arr[i] = true;
    		}	
    	}
    	
    	int M = Integer.parseInt(br.readLine());
    	for (int m=0; m<M; m++) {
    		st = new StringTokenizer(br.readLine());
    		int s = Integer.parseInt(st.nextToken());
    		int i = Integer.parseInt(st.nextToken());
    		if (s == 1) {
    			for (int j=i; j<=N; j+=i) {
    				arr[j] = !arr[j];
    			}
    		} else {
    			int d = 0;
    			while (i-d>=1 && i+d<=N && arr[i-d] == arr[i+d]) {
    				d++;
    			}
    			d--;
    			for (int j=i-d; j<=i+d; j++) {
    				arr[j] = !arr[j];
    			}
    		}
    	}
    	
    	for (int i=1; i<=N; i++) {
    		if (arr[i]) {
    			sb.append(1);
    		} else {
    			sb.append(0);
    		}
    		sb.append(" ");
    		if (i%20 == 0) {
    			sb.append("\n");
    		}
    	}
    	
    	System.out.println(sb.toString());
    	
    	
    }
    

        
}