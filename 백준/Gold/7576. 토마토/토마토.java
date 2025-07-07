import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static class Node {
		
		int r,c,day;
		
		public Node(int r, int c, int day) {
			super();
			this.r = r;
			this.c = c;
			this.day = day;
		}

		@Override
		public String toString() {
			return "Node [r=" + r + ", c=" + c + ", day=" + day + "]";
		}
		
	}

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int M = Integer.parseInt(st.nextToken());
		int N = Integer.parseInt(st.nextToken());
		
		int[][] map = new int[N][M];
		
		int total = 0;
		Queue<Node> q = new ArrayDeque<>();
		
		for (int r=0; r<N; r++) {
			st = new StringTokenizer(br.readLine());
			for (int c=0; c<M; c++) {
				map[r][c] = Integer.parseInt(st.nextToken());
				if (map[r][c] == 0) {
					total++;
				} else if (map[r][c] == 1) {
					q.offer(new Node(r,c,0));
				}
			}
		}

		int[][] dir = {{0,-1},{0,1},{-1,0},{1,0}};
		
		int sol = 0;
		
		outer :
		while (!q.isEmpty()) {
			
			Node cur = q.poll();
//			System.out.println(cur);
			
			for (int d=0; d<4; d++) {
				
				int nr = cur.r+dir[d][0];
				int nc = cur.c+dir[d][1];
				
				if (nr < N && nc < M && nr >= 0 && nc >= 0 && map[nr][nc] == 0) {
					map[nr][nc] = 1;
					if (--total == 0) {
						sol = cur.day+1;
						break outer;
					}
					q.offer(new Node(nr, nc, cur.day+1));
				}

			}
			
		}
		
		if (total == 0) {
			System.out.println(sol);
		} else {
			System.out.println(-1);
		}

	}

}

