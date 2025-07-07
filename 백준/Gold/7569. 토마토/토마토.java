import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static int[][] dir = {{1,0,0},{-1,0,0},{0,1,0},{0,-1,0},{0,0,1},{0,0,-1}};
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int M = Integer.parseInt(st.nextToken());
		int N = Integer.parseInt(st.nextToken());
		int H = Integer.parseInt(st.nextToken());
		
		int[][][] map = new int[H][N][M];
		
		Queue<int[]> q = new ArrayDeque<>();
		
		int total = 0;
		
		for (int h=0; h<H; h++) {
			for (int n=0; n<N; n++) {
				st = new StringTokenizer(br.readLine());
				for (int m=0; m<M; m++) {
					map[h][n][m] = Integer.parseInt(st.nextToken());
					if (map[h][n][m] == 1) {
						q.offer(new int[]{h,n,m,0});
					} else if (map[h][n][m] == 0) {
						total++;
					}
						
						
				}
			}
		}
		
		int sol = 0;
		
		outer:
		while (!q.isEmpty()) {
			
			int[] cur = q.poll();
			
			for (int d=0; d<6; d++) {
				int nh = cur[0] + dir[d][0];
				int nr = cur[1] + dir[d][1];
				int nc = cur[2] + dir[d][2];
				int nday = cur[3]+1;
				if (nh>=H || nh<0 ||
					nr>=N || nr<0 ||
					nc>=M || nc<0 ||
					map[nh][nr][nc] != 0) continue;
				map[nh][nr][nc] = 1;
				if (--total == 0) {
					sol = nday;
					break outer;
				}
				q.offer(new int[] {nh,nr,nc,nday});
					
			}
			
		}
		
		if (total != 0) {
			System.out.println(-1);
		} else {
			System.out.println(sol);
		}
		
	}
	
}

