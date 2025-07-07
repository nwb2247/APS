import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static class Node {
		int r, c;

		public Node(int r, int c) {
			super();
			this.r = r;
			this.c = c;
		}
		
	}
	
	static final int[][] dir = {{0,1},{0,-1},{1,0},{-1,0}};
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int TC = Integer.parseInt(br.readLine());
		
		for (int tc=1; tc<=TC; tc++) {
			
			st = new StringTokenizer(br.readLine());
			
			int M = Integer.parseInt(st.nextToken());
			int N = Integer.parseInt(st.nextToken());
			int K = Integer.parseInt(st.nextToken());
			
			boolean[][] map = new boolean[N][M];
			
			for (int k=0; k<K; k++) {
				st = new StringTokenizer(br.readLine());
				int c = Integer.parseInt(st.nextToken());
				int r = Integer.parseInt(st.nextToken());				
				map[r][c] = true;
			}
			
			boolean[][] visited = new boolean[N][M];
			
			Queue<Node> q = new ArrayDeque<>();
			
			int cnt = 0;
			
			for (int r=0; r<N; r++) {
				for (int c=0; c<M; c++) {
					if (!map[r][c] || visited[r][c]) continue;
					cnt++;
					q.offer(new Node(r,c));
					while(!q.isEmpty()) {
						Node cur = q.poll();
						for (int d=0; d<4; d++) {
							int nr = cur.r+dir[d][0];
							int nc = cur.c+dir[d][1];
							if (nr>=N || nc>=M || nr<0 || nc<0) continue;
							if (!map[nr][nc] || visited[nr][nc]) continue;
							visited[nr][nc] = true;
							q.offer(new Node(nr, nc));
						}
					}
					
					// print(visited, r, c);
				}
			}
			
			sb.append(cnt).append("\n");
		}
		
		System.out.println(sb.toString());
		
	}
	
	private static void print(boolean[][] arr, int r, int c) {
		System.out.println(r + " " + c);
		for (int i=0; i<arr.length; i++) {
			System.out.println(Arrays.toString(arr[i]));
		}
		System.out.println();
	}
}