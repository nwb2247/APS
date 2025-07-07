import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static class Pos {
		
		int r, c, dist;
		
		Pos (int r, int c, int dist) {
			this.r = r;
			this.c = c;
			this.dist = dist;
		}

		@Override
		public String toString() {
			return "Pos [r=" + r + ", c=" + c + ", dist=" + dist + "]";
		}		
		
	}
	
	static int[][] dir = {{-1,0},{1,0},{0,-1},{0,1}};

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		boolean[][] map = new boolean[N][M];
		
		for (int i=0; i<N; i++) {
			char[] chars = br.readLine().toCharArray();
			for (int j=0; j<M; j++) {
				if (chars[j] == '1') {
					map[i][j] = true;
				}
			}
		}
		
		boolean[][] visited = new boolean[N][M];
		
		Queue<Pos> q = new ArrayDeque<>();
		q.offer(new Pos(0, 0, 1));
		
		while(!q.isEmpty()) {
			Pos cur = q.poll();
			if (visited[cur.r][cur.c]) continue;
			if (cur.r == N-1 && cur.c == M-1) {
				System.out.println(cur.dist);
				return;
			}
			visited[cur.r][cur.c] = true;
			for (int i=0; i<4; i++) {
				int nr = cur.r+dir[i][0];
				int nc = cur.c+dir[i][1];
				if (nr >= N || nc >= M || nr < 0 || nc < 0) continue;
				if (visited[nr][nc] || !map[nr][nc]) continue;
				q.offer(new Pos(nr, nc, cur.dist+1));
			}
		}

	}

}
