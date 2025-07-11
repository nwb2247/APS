import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int[] idx = new int[5];
	static int N;
	static int[] arr;
	static int max = 0;
	
    public static void main(String[] args) throws IOException {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st;
    	
    	N = Integer.parseInt(br.readLine());
    	arr = new int[N];
    	idx[4] = N;
    	st = new StringTokenizer(br.readLine());
    	for (int i=0; i<N; i++) {
    		arr[i] = Integer.parseInt(st.nextToken());
    	}
    	
    	recur(0,0);
    	System.out.println(max);
    	
    }
    
    public static void recur(int cnt, int i) {
    	
    	if (cnt == 4) {
    		cal();
    		return;
    	}
    	
    	for (int j=i; j<=N-4+cnt; j++) {
    		idx[cnt] = j;
    		recur(cnt+1, j+1);
    	}
    	
    }
    
    public static void cal() {
    	int sum = 0;
    	for (int i=0; i<4; i++) {
    		int mul = 1;
    		for (int j=idx[i]; j<idx[i+1]; j++) {
    			mul *= arr[j];
    		}
    		sum += mul;
    	}
    	max = Math.max(max, sum);
    }

        
}