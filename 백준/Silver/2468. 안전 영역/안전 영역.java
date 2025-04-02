import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static int N, sol;
	static int[][] map;
	static boolean[][] visited;
	static int maxScore;
	
	static int[] dr = {0,0,1,-1};
	static int[] dc = {1,-1,0,0};

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		N = Integer.parseInt(br.readLine());
		
		map = new int[N][N];
		for (int r=0; r<N ; r++) {
			st = new StringTokenizer(br.readLine());
			for (int c=0; c<N; c++) {
				map[r][c] = Integer.parseInt(st.nextToken());
				maxScore = Math.max(maxScore, map[r][c]);
			}
		}
		
		for (int s=0; s<=maxScore; s++) {
			search(s);
		}
		
		System.out.println(sol);
		
		
	}
	
	private static void search(int limit) {
		
		int cnt = 0;
		
		visited = new boolean[N][N];
		
		for (int r=0; r<N; r++) {
			for (int c=0; c<N; c++) {
				if (map[r][c] > limit) continue;
				visited[r][c] = true;
			}
		}
		
		for (int r=0; r<N; r++) {
			for (int c=0; c<N; c++) {
				if (visited[r][c]) continue;
				
//				for (int i=0; i<N; i++) {
//					System.out.println(Arrays.toString(visited[i]));
//				}
//				System.out.println();
				
				BFS(r,c,limit);
				cnt++;
			}
		}
		
		sol = Math.max(sol, cnt);
		
	}
	
	private static void BFS(int startR, int startC, int limit) {
		
		Queue<int[]> q = new ArrayDeque<>();
		q.add(new int[] {startR, startC});
		visited[startR][startC] = true;
		
		while (!q.isEmpty()) {
			int[] coord = q.poll();
			int r = coord[0];
			int c = coord[1];
			for (int d=0; d<4; d++) {
				int nr = r+dr[d];
				int nc = c+dc[d];
				if (nr >= N || nc >= N || nr < 0 || nc < 0 || visited[nr][nc]) continue;
				q.add(new int[] {nr, nc});
				visited[nr][nc] = true;
			}
			
		}
		
	}

}
