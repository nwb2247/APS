import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
    public static void main(String[] args) throws IOException {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st;
    	
    	int N = Integer.parseInt(br.readLine());
    	st = new StringTokenizer(br.readLine());
    	int[] arr = new int[6];
    	for (int i=0; i<6; i++) {
    		arr[i] = Integer.parseInt(st.nextToken());
    	}
    	st = new StringTokenizer(br.readLine());
    	int T = Integer.parseInt(st.nextToken());
    	int P = Integer.parseInt(st.nextToken());
    	int Tsum = 0;
    	for (int i : arr) {
    		Tsum += i/T;
    		if (i%T != 0) Tsum++;
    	}
    	System.out.println(Tsum);
    	System.out.println(N/P + " " + N%P);
    	
    }
      
}