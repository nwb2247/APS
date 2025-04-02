import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static int sol;
	static boolean find;
	
	public static void main(String[] args) throws IOException {
		
		// BOJ_1600_말이되고픈원숭이
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int K = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		int W = Integer.parseInt(st.nextToken());
		int H = Integer.parseInt(st.nextToken());
		
		int[][] map = new int[H][W]; // map[j][][] 말 이동기회 j번 사용
		
		for (int r=0; r<H; r++) {
			st = new StringTokenizer(br.readLine());
			for (int c=0; c<W; c++) {
				if (Integer.parseInt(st.nextToken()) == 1) {	
					map[r][c] = -1;						// 벽
				} else {
					map[r][c] = Integer.MAX_VALUE;		// 방문 가능 구역
				}				
			}
		}
		map[0][0] = 0;
		
		int[] drM = {0,1,-1,0};
		int[] dcM = {1,0,0,-1};
		int[] drH = {1,2,-1,-2,-1,-2,1,2};
		int[] dcH = {2,1,2,1,-2,-1,-2,-1};
		
		sol = Integer.MAX_VALUE;
		find = false;
		
		Queue<int[]> curQ = new ArrayDeque<>();
		curQ.add(new int[] {0,0}); // r c cnt;
		
		for (int j=0; j<=K; j++) {
			
//			for (int[] pos : curQ) {
//				System.out.print(Arrays.toString(pos));
//				System.out.println();
//			}
			
			Queue<int[]> nextQ = new ArrayDeque<>();
			int[][] nextMap = new int[H][W];
			for (int r=0; r<H; r++) {
				for (int c=0; c<W; c++) {
					nextMap[r][c] = map[r][c];
				}
			}

			while(!curQ.isEmpty()) {
				
				int[] arr = curQ.poll();
				int r = arr[0];
				int c = arr[1];
				
				for (int d=0; d<4; d++) {
					int nr = r+drM[d];
					int nc = c+dcM[d];
					if (nr<0 || nc<0 || nr>=H || nc>=W) continue;
					if (map[nr][nc] <= map[r][c]+1) continue;
					map[nr][nc] = map[r][c]+1;
					nextMap[nr][nc] = Math.min(nextMap[nr][nc], map[r][c]+1);
					curQ.add(new int[] {nr, nc});
				}
				
				if (j == K) continue;
				for (int d=0; d<8; d++) {
					int nr = r+drH[d];
					int nc = c+dcH[d];
					if (nr<0 || nc<0 || nr>=H || nc>=W) continue;
					if (nextMap[nr][nc] <= map[r][c]+1) continue;
					nextMap[nr][nc] = map[r][c]+1;
					nextQ.add(new int[] {nr, nc});
				}
				
			}
			
			curQ = nextQ;
			map = nextMap;

		}
		
		if (map[H-1][W-1] == Integer.MAX_VALUE) map[H-1][W-1] = -1;
		System.out.println(map[H-1][W-1]);

	}


}





