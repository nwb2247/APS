import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

public class Main {
	
	static final int[][] dir = {{1,0},{-1,0},{0,1},{0,-1}};
			
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		char[][] map = new char[N][];
		
		for (int r=0; r<N; r++) {
			map[r] = br.readLine().toCharArray();
		}
		
//		System.out.println(Arrays.deepToString(map));
		
		boolean[][] visited3 = new boolean[N][N];
		Queue<int[]> q3 = new ArrayDeque<>();
		int cnt3 = 0;
		for (int r=0; r<N; r++) {
			for (int c=0; c<N; c++) {
			
				if (visited3[r][c]) continue;
				char color = map[r][c];
				cnt3++;
				q3.offer(new int[] {r,c});
				
				while (!q3.isEmpty()) {
					int[] cur = q3.poll();
					for (int d=0; d<4; d++) {
						int nr = cur[0] + dir[d][0];
						int nc = cur[1] + dir[d][1];
						if (nr>=N ||nc>=N || nr<0 || nc<0 || visited3[nr][nc]) continue;
						if (map[nr][nc] != color) continue;
						visited3[nr][nc] = true;
						q3.offer(new int[] {nr, nc});
					}
					
				}
				
			}
		}
		
		boolean[][] visited2 = new boolean[N][N];
		Queue<int[]> q2 = new ArrayDeque<>();
		int cnt2 = 0;
		for (int r=0; r<N; r++) {
			for (int c=0; c<N; c++) {
			
				if (visited2[r][c]) continue;
				char color = map[r][c];
				cnt2++;
				q2.offer(new int[] {r,c});
				
				while (!q2.isEmpty()) {
					int[] cur = q2.poll();
					for (int d=0; d<4; d++) {
						int nr = cur[0] + dir[d][0];
						int nc = cur[1] + dir[d][1];
						if (nr>=N ||nc>=N || nr<0 || nc<0 || visited2[nr][nc]) continue;
						if (color == 'B') {
							if (map[nr][nc] != 'B') continue;
						} else {
							if (map[nr][nc] == 'B') continue;
						}
						visited2[nr][nc] = true;
						q2.offer(new int[] {nr, nc});
					}
					
				}
				
			}
		}
		
		System.out.println(cnt3 + " " + cnt2);
		
	}
}