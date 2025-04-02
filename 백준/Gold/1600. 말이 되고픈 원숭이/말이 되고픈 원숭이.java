import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static int K, W, H;
	static int[][][] map;
	
	static int[] drM = {0,1,-1,0}; // 2 2
	static int[] dcM = {1,0,0,-1};
	
	static int[] drH = {1,2,-1,-2,-1,-2,1,2}; // 2 6
	static int[] dcH = {2,1,2,1,-2,-1,-2,-1};
	
	static int sol;
	static boolean find;
	
	public static void main(String[] args) throws IOException {
		
		// BOJ_1600_말이되고픈원숭이
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		K = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		W = Integer.parseInt(st.nextToken());
		H = Integer.parseInt(st.nextToken());
		
		map = new int[K+1][H][W]; // map[j][][] 말 이동기회 j번 남음
		
		for (int r=0; r<H; r++) {
			st = new StringTokenizer(br.readLine());
			for (int c=0; c<W; c++) {
				int val = Integer.parseInt(st.nextToken());
				for (int j=0; j<=K; j++) {
					if (val == 1) {
						map[j][r][c] = -1;
					} else {
						map[j][r][c] = Integer.MAX_VALUE-1;
					}
				}
			}
		}
		// 1: 벽 0: 방문가능 (방문할 때마다 -1, 최대값으로 갱신)
		
		sol = Integer.MAX_VALUE;
		find = false;
		// -------------------------------------------
		
		ArrayList<Queue<int[]>> qList = new ArrayList<>();
		for (int j=0; j<=K; j++) {
			qList.add(new ArrayDeque<>());
		}
		
		qList.get(0).add(new int[] {0,0,0}); // r c cnt;
		
		for (int j=0; j<=K; j++) {
//			System.out.println("h");
//			System.out.println(qList.get(j).size());

			while(!qList.get(j).isEmpty()) {
				
				int[] arr = qList.get(j).poll();
				int r = arr[0];
				int c = arr[1];
				int cnt = arr[2];
				
				if (r == H-1 && c == W-1) {
					find = true;
					sol = Math.min(sol, cnt);
//					System.out.println(j + " " +  sol);
				}
				
				for (int d=0; d<4; d++) {
					int nr = r+drM[d];
					int nc = c+dcM[d];
					if (nr<0 || nc<0 || nr>=H || nc>=W) continue;
					if (map[j][nr][nc] <= cnt+1) continue; // 기존의 -cnt(음수)가 현재 위치 -cnt-1보다 크다면 pass; 
					map[j][nr][nc] = cnt+1;
					qList.get(j).add(new int[] {nr, nc, cnt+1});
				}
				
				if (j == K) continue;
				for (int d=0; d<8; d++) {
					int nr = r+drH[d];
					int nc = c+dcH[d];
					if (nr<0 || nc<0 || nr>=H || nc>=W) continue;
					if (map[j+1][nr][nc] <= cnt+1) continue;
					map[j+1][nr][nc] = cnt+1;
					qList.get(j+1).add(new int[] {nr, nc, cnt+1});
				}
				
			}
			
//			System.out.println(Arrays.deepToString(map[j]));
			
			if (j == K) continue;
			for (int r=0; r<H; r++) {
				for (int c=0; c<W; c++) {
					map[j+1][r][c] = Math.min(map[j+1][r][c], map[j][r][c]);
				}
			}
		}
		
		
		
		
		
		
		
		if (find) {
			System.out.println(sol);
		} else {
			System.out.println(-1);
		}

	}
	
//	private static void DFS(int r, int c, int k, int cnt) {
//		
//		if (r == H-1 && c == W-1) {
//			find = true;
//			sol = Math.min(sol, cnt);
//		}
//		
//		// k==0 여부와 상관없이 상하좌우 이동가능(원숭이)
//		for (int d=0; d<4; d++) {
//			int nr = r+drM[d];
//			int nc = c+dcM[d];
//			if (nr<0 || nc<0 || nr>=H || nc>=W) continue;
//			if (map[nr][nc]) continue;
//			map[nr][nc] = true;
//			DFS(nr, nc, k, cnt+1);
//			map[nr][nc] = false; // 원상복구
//		}
//		if (k <= 0) return;
//		for (int d=0; d<8; d++) {
//			int nr = r+drH[d];
//			int nc = c+dcH[d];
//			if (nr<0 || nc<0 || nr>=H || nc>=W) continue;
//			if (map[nr][nc]) continue;
//			map[nr][nc] = true;
//			DFS(nr, nc, k-1, cnt+1);
//			map[nr][nc] = false; // 원상복구
//		}
//		
//	}

}





