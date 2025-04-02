import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
	
	static int N;
	static int[][] map;

	public static void main(String[] args) throws IOException {
		
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		for (int t=1; t<=T; t++) {
			
			// 입력 부분
			N = Integer.parseInt(br.readLine());
			map = new int[N][N];
			for (int r=0; r<N; r++) {
				String[] line = br.readLine().split("");
				for (int c=0; c<N; c++) {
					map[r][c] = Integer.parseInt(line[c]);
				}
			}
//			System.out.println(Arrays.deepToString(map));
			
			// 풀이 부분
			int sum = 0;
			for (int r=0; r<=N/2; r++) {
				for (int c=N/2-r; c<=N/2+r; c++) {
					sum += map[r][c];
				}
			}
			
			for (int k=0; k<=N/2-1; k++) {
				for (int c=N/2-k; c<=N/2+k; c++) {
					sum += map[N-1-k][c];
				}
			}
			
			sb.append("#"+t+" "+sum+"\n");
			
		}
		
		System.out.println(sb);

	}

}
