import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static final int[][] dir = {{1,0},{-1,0},{0,1},{0,-1}};
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		int R = Integer.parseInt(st.nextToken());
		int C = Integer.parseInt(st.nextToken());
		
		int[][] map = new int[R][C];
		
		int[] start = new int[2];
		for (int r=0; r<R; r++) {
			st = new StringTokenizer(br.readLine());
			for (int c=0; c<C; c++) {
				int val = Integer.parseInt(st.nextToken());
				switch(val) {
				case 2 :
					start[0] = r; start[1] = c;
				case 1 :
					map[r][c] = val-2;
					break;
				}
			}
		}
		
		Queue<int[]> q = new ArrayDeque<>();
		q.offer(start);
		while (!q.isEmpty()) {
			int[] cur = q.poll();
			for (int d=0; d<4; d++) {
				int nr = cur[0] + dir[d][0];
				int nc = cur[1] + dir[d][1];
				if (nr<0 || nc<0 || nr>=R || nc>=C || map[nr][nc] != -1) continue;
				map[nr][nc] = map[cur[0]][cur[1]]+1;
				q.offer(new int[] {nr, nc});
			}
			
		}
		
		for (int r=0; r<R; r++) {
			for (int c=0; c<C; c++) {
				sb.append(map[r][c]).append(" ");
			}
			sb.append("\n");
		}
		System.out.println(sb.toString());

		
	}
}
