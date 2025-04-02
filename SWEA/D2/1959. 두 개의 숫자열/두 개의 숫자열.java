import java.io.*;
import java.util.*;

class Solution {
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		for(int t=1; t<=T; t++) {
			
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			
			int[] A = new int[N];
			int[] B = new int[M];
			
			st = new StringTokenizer(br.readLine(), " ");
			for(int i=0; i<N; i++) {
				A[i] = Integer.parseInt(st.nextToken());
			}
			
			st = new StringTokenizer(br.readLine(), " ");
			for(int i=0; i<M; i++) {
				B[i] = Integer.parseInt(st.nextToken());
			}
			
			int[] S;
			int[] L;
			if(N<M) {
				S = A; L = B;
			} else {
				S = B; L = A;
			}
			
			int max = 0;
			for(int i=0; i<=L.length-S.length; i++) {
				int sum = 0;
				for(int j=0; j<S.length; j++) {
					sum += S[j]*L[j+i];
				}
				max = Math.max(max, sum);
			}
			
			System.out.println("#" + t + " " +max);
 		}
	}
}