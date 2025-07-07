import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static int[][] dir = {{-2,1},{-1,2},{1,2},{2,1},{2,-1},{1,-2},{-1,-2},{-2,-1}};
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int TC = Integer.parseInt(br.readLine());		
		for (int tc=1; tc<=TC; tc++) {
			
			int N = Integer.parseInt(br.readLine());
			
			Queue<int[]> q = new ArrayDeque<>();
			
			int[][] map = new int[N][N];
			for (int r=0; r<N; r++) {
				Arrays.fill(map[r], -1);
			}
			
			st = new StringTokenizer(br.readLine());
			int[] start = new int[2];
			start[0] = Integer.parseInt(st.nextToken());
			start[1] = Integer.parseInt(st.nextToken());
			q.offer(start);
			map[start[0]][start[1]] = 0;
			
			
			st = new StringTokenizer(br.readLine());
			int[] dest = new int[2];
			dest[0] = Integer.parseInt(st.nextToken());
			dest[1] = Integer.parseInt(st.nextToken());
			
			int sol = 0;
			
			while(!q.isEmpty()) {
				
				int[] cur = q.poll();
				
				if (cur[0] == dest[0] && cur[1] == dest[1]) {
					sol = map[dest[0]][dest[1]];
					break;
				}
				
				for (int d=0; d<8; d++) {
					int nr = cur[0]+dir[d][0];
					int nc = cur[1]+dir[d][1];
					if (nr>=N || nc>=N || nr<0 || nc<0 || map[nr][nc]!=-1) continue;
					map[nr][nc] = map[cur[0]][cur[1]]+1;
					q.offer(new int[] {nr, nc});
				}
				
			}
			
			sb.append(sol).append("\n");

		}
		
		System.out.println(sb.toString());
		
	}
	
}

