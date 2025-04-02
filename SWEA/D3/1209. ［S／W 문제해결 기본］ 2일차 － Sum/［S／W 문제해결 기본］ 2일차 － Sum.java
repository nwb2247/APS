import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws IOException {
		
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = 100;
		for (int i=1; i<=10; i++) {
			int t = Integer.parseInt(br.readLine());
			
			int[][] map = new int[N][N];
			
			for (int r=0; r<N; r++) {
				st = new StringTokenizer(br.readLine());
				for (int c=0; c<N; c++) {
					map[r][c] = Integer.parseInt(st.nextToken());
				}
			}
			
			// 최대값 구하기
			int max = Integer.MIN_VALUE;
			for (int r=0; r<N; r++) { // 행합
				int sum = 0;
				for (int c=0; c<N; c++) {
					sum += map[r][c];
				}
				max = Math.max(max, sum);
			}
			
			for (int c=0; c<N; c++) { // 열합
				int sum = 0;
				for (int r=0; r<N; r++) {
					sum += map[r][c];
				}
				max = Math.max(max, sum);
			}
			
			int sum = 0;
			for (int k=0; k<N; k++) {
				sum += map[k][k];
			}
			max = Math.max(max, sum);
			
			sum = 0;
			for (int k=0; k<N; k++) {
				sum += map[k][N-1-k];
			}
			max = Math.max(max, sum);
			
			System.out.println("#" + t + " " + max);
			
		}

	}

}
