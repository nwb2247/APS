import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solution {
	
	static int N, K, pH;
	static int[][] map;
	static ArrayList<int[]> pList;
	
	static int[] dr = {-1,0,1,0};
	static int[] dc = {0,1,0,-1};
	
	static int sol;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		
		
		int T = Integer.parseInt(br.readLine());
		
		for (int t=1; t<=T; t++) {
			
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			K = Integer.parseInt(st.nextToken());
			pH = 0;
			map = new int[N][N];
			
			pList = new ArrayList<>();
			for (int r=0; r<N; r++) {
				st = new StringTokenizer(br.readLine());
				for (int c=0; c<N; c++) {
					map[r][c] = Integer.parseInt(st.nextToken());
					if (map[r][c] < pH) continue;
					if (map[r][c] > pH) {
						pList.clear();
						pH = map[r][c];
					}
						
					pList.add(new int[] {r,c});
				}
			}
			
			sol = 0;
			
			// 맨 처음 하나도 깎지 않고 확인
			makePath();
			
			// 각 요소(봉우리 후보 포함) 돌면서 1~5까지 깎으면서 확인
			for (int r=0; r<N; r++) {
				for (int c=0; c<N; c++) {
					int originH = map[r][c];
					for (int i=1; i<=K; i++) {
						map[r][c] = originH-i;
						makePath();
					}
					// 원상복구
					map[r][c] = originH;
				}
			}
			
			sb.append("#").append(t).append(" ").append(sol).append("\n");
			
		}
		
		System.out.println(sb.toString());

	}
	
	private static void makePath() {
		for (int[] p : pList) {
			DFS(p[0], p[1], 1);
		}
	}
	
	private static void DFS(int r, int c, int len) {
		
		sol = Math.max(sol, len);
		
		for (int d=0; d<4; d++) {
			int nr = r+dr[d];
			int nc = c+dc[d];
			if (nr < 0 || nc < 0 || nr >= N || nc >= N) continue;
			if (map[nr][nc] >= map[r][c]) continue;
			DFS(nr, nc, len+1);
		}
		
	}

}
