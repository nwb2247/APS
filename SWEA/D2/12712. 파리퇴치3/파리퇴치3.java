import java.io.*;
import java.util.*;

class Solution {
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		for(int t=1; t<=T; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			
			int[][] mat = new int[N][N];
			
			
			for(int r=0; r<N; r++) {
				StringTokenizer rowst = new StringTokenizer(br.readLine());
				for(int c=0; c<N; c++) {
					mat[r][c] = Integer.parseInt(rowst.nextToken());
				}
			}
			
			int max = 0;
			for(int r=0; r<N; r++) {
				for(int c=0; c<N; c++) {
					
					int sumCross = 0, sumX = 0;
					int top = Math.max(0, r-(M-1));
					int bottom = Math.min(N-1, r+(M-1));
					int left = Math.max(0, c-(M-1));
					int right = Math.min(N-1, c+(M-1));
					
					for(int i=r; i<=bottom; i++) {
						sumCross += mat[i][c];
					}
					for(int i=r; i>=top; i--) {
						sumCross += mat[i][c];
					}
					for(int i=c; i<=right; i++) {
						sumCross += mat[r][i];
					}
					for(int i=c; i>=left; i--) {
						sumCross += mat[r][i];
					}
					sumCross -= 3*mat[r][c];
					
					int i = r, j = c;
					while(i<=bottom && j<=right) {
						sumX += mat[i][j];
						i++; j++;
					}
					i = r; j = c;
					while(i>=top && j<=right) {
						sumX += mat[i][j];
						i--; j++;
					}
					i = r; j = c;
					while(i<=bottom && j>=left) {
						sumX += mat[i][j];
						i++; j--;
					}
					i = r; j = c;
					while(i>=top && j>=left) {
						sumX += mat[i][j];
						i--; j--;
					}
					sumX -= 3*mat[r][c];
					
					max = Math.max(max, Math.max(sumCross, sumX));
				}
			}
			System.out.println("#" + t + " " + max);
		}
	}
}