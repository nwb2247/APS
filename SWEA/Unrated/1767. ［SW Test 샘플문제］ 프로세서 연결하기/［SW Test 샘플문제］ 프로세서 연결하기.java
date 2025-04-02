import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solution {
	
	static int N;
	static ArrayList<int[]> cList;
	
	static int[] dr = {-1,0,1,0};
	static int[] dc = {0,1,0,-1};
	static int[][] map;
	
	static int cMax, lenMin;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		
		for (int t=1; t<=T; t++) {
			N = Integer.parseInt(br.readLine());
			map = new int[N][N];
			cList = new ArrayList<>();
			
			for (int r=0; r<N; r++) {
				st = new StringTokenizer(br.readLine());
				for (int c=0; c<N; c++) {
					map[r][c] = Integer.parseInt(st.nextToken());
					if (map[r][c] == 0) continue;
					if (r == 0 || r == N-1 || c == 0 || c == N-1) continue;
					cList.add(new int[] {r,c});
				}
			}
			
			cMax = 0;
			lenMin = Integer.MAX_VALUE;
			
			BT(0, 0, 0);
			
			sb.append("#").append(t).append(" ").append(lenMin).append("\n");
			
		}
		
		System.out.println(sb.toString());

	}
	
	private static void BT(int idx, int cCnt, int len) {
		
		if (idx == cList.size()) {
			if (cCnt == cMax) {
				lenMin = Math.min(lenMin, len);
			} else if (cCnt > cMax) {
				cMax = cCnt;
				lenMin = len;
			}
			return;
		}
		
		int cR = cList.get(idx)[0];
		int cC = cList.get(idx)[1];
		
		int[] originR = new int[N];
		int[] originC = new int[N];
		
		for (int i=0; i<N; i++) {
			originR[i] = map[cR][i];
			originC[i] = map[i][cC];
		}
		
		BT(idx+1, cCnt, len);
		
		for (int d=0; d<4; d++) {

			int r = cR+dr[d];
			int c = cC+dc[d];
			boolean available = false;
			while(true) {
				if (r < 0 || r >= N || c < 0 || c >= N) {
					available = true;
					break;
				}
				if (map[r][c] != 0) break;
				r += dr[d];
				c += dc[d];
			}
			
			if (!available) continue;
			r = cR+dr[d];
			c = cC+dc[d];
			int newL = 0;
			while(r >= 0 && r < N && c >= 0 && c < N) {
				newL++;
				map[r][c] = 1;
				r += dr[d];
				c += dc[d];
			}
			
			BT(idx+1, cCnt+1, len+newL);
			
			if (d%2 == 0) {
				for (int i=0; i<N; i++) {
					map[i][cC] = originC[i];
				}
			} else {
				for (int i=0; i<N; i++) {
					map[cR][i] = originR[i];
				}
			}
			
		}
		
		
	}

}
