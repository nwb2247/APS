import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Solution {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		for (int t=1; t<=T; t++) {
			int N = Integer.parseInt(br.readLine());
			
			int[][] map = new int[N][N];
			
			int[] dr = {0,1,0,-1};
			int[] dc = {1,0,-1,0};
			
			int d = 0;
			int c = 0;
			int r = 0;
			
			for (int i=1; i<=N*N; i++) {
				
				map[r][c] = i;
				int nr = r + dr[d];
				int nc = c + dc[d];
				if (nr >= N || nr < 0 || nc >= N || nc < 0 || map[nr][nc] != 0) {
					d = (d+1)%4;
					nr = r + dr[d];
					nc = c + dc[d];
				}
				r = nr;
				c = nc;
			}
			
			StringBuilder sb = new StringBuilder();
			sb.append("#"+t+"\n");
			for (int i=0; i<N; i++) {
				for (int j=0; j<N; j++) {
					sb.append(map[i][j]+ " ");
				}
				sb.append("\n");
			}
			
			System.out.println(sb.toString().trim());
			
			
		}
		

	}

}
