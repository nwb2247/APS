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
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		while (true) {
			
			st = new StringTokenizer(br.readLine());
			int L = Integer.parseInt(st.nextToken());
			int R = Integer.parseInt(st.nextToken());
			int C = Integer.parseInt(st.nextToken());
			
			if (L==0 && R==0 && C==0) break;
			
			int[] S = new int[3];
			
			char[][][] map = new char[L][R][C];
			
			for (int l=0; l<L; l++) {
				for (int r=0; r<R; r++) {
					map[l][r] = br.readLine().toCharArray();
					for (int c=0; c<C; c++) {
						if (map[l][r][c] == 'S') {
							S[0] = l; S[1] = r; S[2] = c;
						}
					}
				}
				br.readLine();
			}
			
			int[][][] visited = new int[L][R][C];
			for (int l=0; l<L; l++) {
				for (int r=0; r<R; r++) {
					for (int c=0; c<C; c++) {
						Arrays.fill(visited[l][r], -1);
					}
				}
			}
			visited[S[0]][S[1]][S[2]] = 0;
			
			Queue<int[]> q = new ArrayDeque<>();
			
			q.offer(S);
			int sol = 0;
			outer:
			while (!q.isEmpty()) {
				
				int[] cur = q.poll();
				
				for (int d=0; d<6; d++) {
					int nl = cur[0]+dir[d][0];
					int nr = cur[1]+dir[d][1];
					int nc = cur[2]+dir[d][2];
//					System.out.println(nl + " " + nr + " " + nc);
					int nm = visited[cur[0]][cur[1]][cur[2]]+1;
					if (nl>=L || nr>=R || nc>=C || nl<0 || nr<0 || nc<0) continue;
					if (map[nl][nr][nc] == 'E') {
						sol = nm;
						break outer;
					}
					if (map[nl][nr][nc] == '#' || visited[nl][nr][nc] != -1) continue;
					visited[nl][nr][nc] = nm;
					q.offer(new int[] {nl, nr, nc});
				}
			}
			if (sol == 0) {
				sb.append("Trapped!").append("\n");
			} else {
				sb.append("Escaped in ").append(sol).append(" minute(s).").append("\n");
			}
			
		}
		
		System.out.println(sb.toString());

	}
	
}

