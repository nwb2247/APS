import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static final int[][] dir = {{1,0},{-1,0},{0,-1},{0,1}};
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int TC = Integer.parseInt(br.readLine());
		
		for (int tc=1; tc<=TC; tc++) {
			st = new StringTokenizer(br.readLine());
			int C = Integer.parseInt(st.nextToken());
			int R = Integer.parseInt(st.nextToken());
			
			char[][] map = new char[R][];
			
			boolean[][] visited = new boolean[R][C];
			
			Queue<int[]> fq = new ArrayDeque<>();
			Queue<int[]> sq = new ArrayDeque<>();
			
			for (int r=0; r<R; r++) {
				map[r] = br.readLine().toCharArray();
				for (int c=0; c<C; c++) {
					switch(map[r][c]) {
					case '@' :
						sq.offer(new int[] {r, c, 0});
						map[r][c] = '.';
						visited[r][c] = true;
						break;
					case '*' :
						fq.offer(new int[] {r, c, 0});
						break;
					}
				}
			}
			
//			for (int r=0; r<R; r++) {
//				System.out.println(Arrays.toString(map[r]));
//			}
//			System.out.println();
			
			int sec = 0;
			int sol = -1;
			
			outer:
			while(!sq.isEmpty()) {
				
				while (!fq.isEmpty() && fq.peek()[2] == sec) {
					int[] cur = fq.poll();
					for (int d=0; d<4; d++) {
						int nr = cur[0]+dir[d][0];
						int nc = cur[1]+dir[d][1];
						if (nr>=R || nc>=C || nr<0 || nc<0 || map[nr][nc] != '.') continue;
						map[nr][nc] = '*';
						fq.offer(new int[] {nr, nc, sec+1});
					}
				}
				
				while (!sq.isEmpty() && sq.peek()[2] == sec) {
					int[] cur = sq.poll();
					
					if (cur[0]==R-1 || cur[1]==C-1 || cur[0]==0 || cur[1]==0) {
						sol = sec+1;
						break outer;
					}
					
					for (int d=0; d<4; d++) {
						int nr = cur[0]+dir[d][0];
						int nc = cur[1]+dir[d][1];
						if (nr>=R || nc>=C || nr<0 || nc<0 || map[nr][nc] != '.' || visited[nr][nc]) continue;
						visited[nr][nc] = true;
						sq.offer(new int[] {nr, nc, sec+1});
					}
				}
				
//				for (int r=0; r<R; r++) {
//					System.out.println(Arrays.toString(map[r]));
//				}
//				System.out.println();
				
				sec++;
				
			}
			
			if (sol == -1) {
				sb.append("IMPOSSIBLE").append("\n");
			} else {
				sb.append(sol).append("\n");
			}
			
		}
		
		System.out.println(sb.toString());
		
	}
}

