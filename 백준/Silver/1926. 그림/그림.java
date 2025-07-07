import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static class Pos {
		
		int r, c;
		
		Pos (int r, int c) {
			this.r = r;
			this.c = c;
		}

		@Override
		public String toString() {
			return "Pos [r=" + r + ", c=" + c + "]";
		}
		
		
	}

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		boolean[][] map = new boolean[N][M];
		
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j=0; j<M; j++) {
				if (Integer.parseInt(st.nextToken()) == 1) {
					map[i][j] = true;
				}
			}
		}
		
		int[][] dir = {{-1,0},{1,0},{0,-1},{0,1}};
		
		boolean[][] visited = new boolean[N][M];
		
		int maxCnt = 0;
		int num = 0;
		
		for (int r=0; r<N; r++) {
			for (int c=0; c<M; c++) {
				if (visited[r][c] || !map[r][c]) continue;
				
				Queue<Pos> q = new ArrayDeque<>();
				q.offer(new Pos(r,c));
				
				int cnt = 0;
				num++;
				
				while(!q.isEmpty()) {
					Pos cur = q.poll();
					if (visited[cur.r][cur.c]) continue;
					cnt++;
					visited[cur.r][cur.c] = true;
					for (int i=0; i<4; i++) {
						int nr = cur.r+dir[i][0];
						int nc = cur.c+dir[i][1];
						if (nr >= N || nc >= M || nr < 0 || nc < 0) continue;
						if (visited[nr][nc] || !map[nr][nc]) continue;
						q.offer(new Pos(nr, nc));
					}
				}

				maxCnt = Math.max(maxCnt, cnt);				
				
			}
		}
		
		System.out.println(num + "\n" + maxCnt);
		

	}

}
