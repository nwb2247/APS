import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws IOException {
		
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		
		int T = sc.nextInt();
		
		for (int t=1; t<=T; t++) {
			
			int N = sc.nextInt();
			int[] h = new int[N];
			
			for (int i=0; i<N; i++) {
				h[i] = sc.nextInt();
			}
			
			int ascending = 0;
			boolean isAscending = false;
			
			int sum = 0;
			
			for (int i=1; i<N; i++) {
				
				if (h[i] > h[i-1]) {
					if (!isAscending) {			// ascending
						isAscending = true;
						ascending = 0;
					} 
					ascending++;
				} else {						// descending
					if (isAscending) {
						isAscending = false;
					}
					sum += ascending;
				}
				
			}
			
			sb.append("#"+t+" "+sum+"\n");
		}	
		
		System.out.println(sb);

	}
	
	

}
