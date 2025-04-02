import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
	
	static int N, M, C;
	static int[][] map;
	static int[][] map2;
	
	static int[][] profits;
	static int[] block;

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		
		for (int t=1; t<=T; t++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			C = Integer.parseInt(st.nextToken());
			map = new int[N][N];
			map2 = new int[N][N];
			for (int r=0; r<N; r++) {
				st = new StringTokenizer(br.readLine());
				for (int c=0; c<N; c++) {
					map[r][c] = Integer.parseInt(st.nextToken());
					map2[r][c] = map[r][c] * map[r][c];
				}
			}
			
//			System.out.println(Arrays.deepToString(map));
//			System.out.println(N + " " + M + " " + C);
			profits = new int[N][N-M+1];
			block = new int[M];
			
			for (int r=0; r<N; r++) {
				for (int c=0; c<N-M+1; c++) {
					findMaxProfit(r, c, c, 0, 0, 0);
				}
			}
			
//			System.out.println(Arrays.deepToString(profits));
			
			int sol = 0;
			for (int i=0; i<N*(N-M+1); i++) {
				int iR = i/(N-M+1);
				int iC = i%(N-M+1);
				for (int j=i+1; j<N*(N-M+1); j++) {
					int jR = j/(N-M+1);
					int jC = j%(N-M+1);
					if (iR == jR && jC-iC < M) continue;
					sol = Math.max(sol, profits[iR][iC] + profits[jR][jC]);
				}
			}
			
			sb.append("#").append(t).append(" ").append(sol).append("\n");
			
		}
		
		System.out.println(sb.toString());
	

	}
	
	
	private static void findMaxProfit(int r, int c, int start, int cnt, int sum, int profit) {
		
		profits[r][c] = Math.max(profits[r][c], profit); 
		
		if (cnt == M) {
//			System.out.println(Arrays.toString(block));
			return;
		}		
		
		for (int i=start; i<c+M; i++) {
			if (sum+map[r][i] > C) continue;
			block[cnt] = map[r][i];
			findMaxProfit(r, c, i+1, cnt+1, sum+map[r][i], profit+map2[r][i]);
		}
	}

}
