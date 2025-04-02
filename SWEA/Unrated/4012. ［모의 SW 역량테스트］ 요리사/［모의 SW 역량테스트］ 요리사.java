import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
	
	static int N;
	static int[][] matrix;
	
	static boolean[] isSelected;
	static int min;
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		
		for (int t=1; t<=T; t++) {
			
			N = Integer.parseInt(br.readLine());
			
			matrix = new int[N][N];
			
			for (int r=0; r<N; r++) {
				st = new StringTokenizer(br.readLine());
				for (int c=0; c<N; c++) {
					matrix[r][c] = Integer.parseInt(st.nextToken());
				}
			}
			
			isSelected = new boolean[N];
			min = Integer.MAX_VALUE;
			comb(0, 0);
			sb.append("#"+ t + " " + min + "\n");
			
			
			
		}
		
		System.out.println(sb);
			
		
	}
	
	private static void comb(int cnt, int startIdx) {
		
		if (cnt == N/2) {
			int A = calculate(false);
			int B = calculate(true);
			
			min = Math.min(min, Math.abs(A-B));
			
			return;
		}
		
		for (int i=startIdx; i<N; i++) {
			isSelected[i] = true;
			comb(cnt+1, i+1);
			isSelected[i] = false;
		}
		
	}
	
	private static int calculate(boolean bool) {
		int sum = 0;
		for (int i=0; i<N; i++) {
			if (isSelected[i] != bool) continue;
			for (int j=0; j<N; j++) {
				if (isSelected[j] == bool) sum += matrix[i][j];
			}
		}
		
		return sum;
	}
	
}
