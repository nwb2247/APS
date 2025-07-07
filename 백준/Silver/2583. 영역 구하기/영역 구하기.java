import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static int[][] dir = {{0,1},{0,-1},{1,0},{-1,0}};
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		int M = Integer.parseInt(st.nextToken());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		boolean[][] map = new boolean[M][N];
		
		for (int k=0; k<K; k++) {
			st = new StringTokenizer(br.readLine());
			int c1 = Integer.parseInt(st.nextToken());
			int r1 = Integer.parseInt(st.nextToken());
			int c2 = Integer.parseInt(st.nextToken());
			int r2 = Integer.parseInt(st.nextToken());
			for (int r=r1; r<r2; r++) {
				for (int c=c1; c<c2; c++) {
					map[r][c] = true;
				}
			}
		}
		
		int cnt = 0;
		Queue<int[]> q = new ArrayDeque<>();
		
		List<Integer> l = new ArrayList<>();
		
		for (int r=0; r<M; r++) {
			for (int c=0; c<N; c++) {
				if (map[r][c]) continue;
				cnt++;
				int size = 0;
				map[r][c] = true;
				q.offer(new int[] {r,c});
				while(!q.isEmpty()) {
					int[] cur = q.poll();
					size++;
					for (int d=0; d<4; d++) {
						int nr = cur[0]+dir[d][0];
						int nc = cur[1]+dir[d][1];
						if (nr>=M || nc>=N || nr<0 || nc<0 || map[nr][nc]) continue;
						map[nr][nc] = true;
						q.offer(new int[] {nr,nc});
					}	
				}
				l.add(size);
			}
		}
		
		Collections.sort(l);
		sb.append(cnt).append("\n");
		for (int v : l) {
			sb.append(v).append(" ");
		}
		System.out.println(sb.toString());

	}
	
}
