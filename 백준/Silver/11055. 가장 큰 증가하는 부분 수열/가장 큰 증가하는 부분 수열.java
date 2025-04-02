import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	 public static void main(String[] args) throws IOException {
		
		 BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		 
		 int N = Integer.parseInt(br.readLine());
		 
		 int[] arr = new int[N];
		 int[] DP = new int[N];
		 
		 StringTokenizer st = new StringTokenizer(br.readLine());
		 
		 int max = 0;
		 for (int i=0; i<N; i++) {
			 arr[i] = Integer.parseInt(st.nextToken());
			 for (int j=0; j<i; j++) {
				 if (arr[j] < arr[i]) {
					 DP[i] = Math.max(DP[i], DP[j]);
 				 }
			 }
			 DP[i] += arr[i];
			 max = Math.max(max, DP[i]);
		 }

		 System.out.println(max);		  
		 
	}
}
