import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
	
	static int N, W, H;
	static int[][] dir = new int[][] {{0,1},{1,0},{0,-1},{-1,0}};
	
	static int sol;
	static boolean visited[];

	static int[][] mmm;

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st; 
		StringBuilder sb = new StringBuilder();
		
		int TC = Integer.parseInt(br.readLine());
		for (int tc=1; tc<=TC; tc++) {
			
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			W = Integer.parseInt(st.nextToken());
			H = Integer.parseInt(st.nextToken());
			
			int[][] map = new int[H][W];
			for (int r=0; r<H; r++) {
				st = new StringTokenizer(br.readLine());
				for (int c=0; c<W; c++) {
					map[r][c] = Integer.parseInt(st.nextToken());
				}
			}
			
			sol = Integer.MAX_VALUE;
			play(0, map);
			sb.append("#").append(tc).append(" ").append(sol).append("\n");
			
		}
		System.out.println(sb.toString());

	}
	
	// 열을 정하여 터트림 (주의 : 선택했던 열을 다시 선택할 수 있으므로, 순열이 아님!)
	private static void play(int cnt, int[][] map) {
		
		if (cnt == N) {
			return;
		}
		
		for (int c=0; c<W; c++) {
			int[][] newMap = copy(map);
			int r=0;
			for (; r<H; r++) {
				if (map[r][c] != 0) break;
			}
			if (r >= H) continue;
			pop(r,c, newMap);
			fall(newMap);
			sol = Math.min(sol, count(newMap));
			play(cnt+1, newMap);
		}
		
	}
	
	// 새 맵 복사
	private static int[][] copy(int[][] map) {
		int[][] ret = new int[H][W];
		for (int r=0; r<H; r++) {
			for (int c=0; c<W; c++) {
				ret[r][c] = map[r][c];
			}
		}
		return ret;
	}
	
	// 다 터뜨린후 공중에 있는 것 아래로 이동시킴
	private static void fall(int[][] map) {
		
		for (int c=0; c<W; c++) {
			int blank = 0;
			for (int r=H-1; r>=0; r--) {
				if (map[r][c] != 0) continue;
				blank = r;
				break;
			}
			
			for (int r=blank-1; r>=0; r--) {
				if (map[r][c] == 0) continue;
				map[blank--][c] = map[r][c];
				map[r][c] = 0;
			}
		}
		
	}
	
	// 폭탄 터짐
	private static void pop(int r, int c, int[][] map) {
		
		if (map[r][c] == 0) {
			return;
		}
		
		int range = map[r][c];
		map[r][c] = 0;
		
		for (int d=0; d<4; d++) {
			for (int i=1; i<=range; i++) {
				int nr = r + (i-1)*dir[d][0];
				int nc = c + (i-1)*dir[d][1];
				if (nr>=H || nc>=W || nr<0 || nc<0) continue;
				pop(nr, nc, map);
			}
		}
		
	}
	
	// 갯수 체크
	private static int count(int[][] map) {
		int ret = 0;
		for (int r=0; r<H; r++) {
			for (int c=0; c<W; c++) {
				if (map[r][c]!=0) ret++;
			}
		}
		return ret;
	}
	
//	private static void print(int[][] map) {
//
//		for (int r=0; r<H; r++) {
//			System.out.println(Arrays.toString(map[r]));
//		}
//		System.out.println();
//
//	}

}
