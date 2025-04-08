import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	
	static int N;
	static int[][] map;
	
	static int[][] d = {{-1,0},{1,0},{0,-1},{0,1}}; // 상0 하1 좌2 우2
	static int[][] turn = {
			{0,1,2,3}, // 벽x
			{1,3,0,2},
			{3,0,1,2},
			{2,0,3,1},
			{1,2,3,0},
			{1,0,3,2}
	};
			
	static int[][][] wormHoles;

	static int startR, startC;
	static int r, c, dir;
	static int max;
	static int score;
	static boolean fin;
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int TC = Integer.parseInt(br.readLine().trim());
		
		for (int tc=1; tc<=TC; tc++) {
			
			N = Integer.parseInt(br.readLine().trim());
			map = new int[N][N];
			
			wormHoles = new int[10+1][2][2];
			for (int i=6; i<=10; i++) {
				for (int j=0; j<2; j++) {
					wormHoles[i][j][0] = -1;
				}
			}
			
			
			for (int r=0; r<N; r++) {
				st = new StringTokenizer(br.readLine().trim());
				for (int c=0; c<N; c++) {
					int val = Integer.parseInt(st.nextToken());
					map[r][c] = val;
					if (val>=6) {
						if (wormHoles[val][0][0] == -1) {
							wormHoles[val][0][0] = r;
							wormHoles[val][0][1] = c;
						} else {
							wormHoles[val][1][0] = r;
							wormHoles[val][1][1] = c;
						}
					}
				}
			}
			
			max = 0;
			
			for (int i=0; i<N; i++) {
				for (int j=0; j<N; j++) {
					if (map[i][j] != 0) continue;
					for (int k=0; k<4; k++) {
						startR = i; startC = j; dir = k;
						r = startR; c = startC;
						score = 0; fin = false;
						move();
						while (!fin) {
							move();
						}
						
					}
				}
			}
			
//			System.out.println(sol);
			sb.append("#").append(tc).append(" ").append(max).append("\n");
			
		}
		
		System.out.println(sb.toString());


	}
	
	private static void move() {

		r += d[dir][0]; c += d[dir][1];
		
//		System.out.println(r + " " + c);
		
		if (r<0 || r>=N || c<0 || c>=N) {
			dir = turn[5][dir];
			score++;
			return;
		}
		
		int val = map[r][c];
		
		if ((r == startR && c == startC) || val == -1) {
			max = Math.max(max, score);
			fin = true;
		} else if (val == 0) {
			return;
		} else if (val <= 5) {
			dir = turn[val][dir];
			score++;
		} else { // val >= 6
			int[] w0 = wormHoles[val][0];
			int[] w1 = wormHoles[val][1];
			if (r == w0[0] && c == w0[1]) {
				r = w1[0];
				c = w1[1];
			} else {
				r = w0[0];
				c = w0[1];
			}
		}

		
	}

}

