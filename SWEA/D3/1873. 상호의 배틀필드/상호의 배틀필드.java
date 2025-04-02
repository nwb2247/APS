import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
	
	static int[] dr = {-1,1,0,0};
	static int[] dc = {0,0,-1,1};
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		
		for (int t=1; t<=T; t++) {
			st = new StringTokenizer(br.readLine());
			int H = Integer.parseInt(st.nextToken());
			int W = Integer.parseInt(st.nextToken());
			
			char[][] map = new char[H][W];
			
			int[] coord = new int[3]; // 0:r 1:c 2:d
			
			for (int r=0; r<H; r++) {
				char[] line = br.readLine().toCharArray();
				for (int c=0; c<W; c++) {
					map[r][c] = line[c];
					if (map[r][c] == '^') {
						coord[0] = r;
						coord[1] = c;
						coord[2] = 0;
					} else if (map[r][c] == 'v') {
						coord[0] = r;
						coord[1] = c;
						coord[2] = 1;
					} else if (map[r][c] == '<') {
						coord[0] = r;
						coord[1] = c;
						coord[2] = 2;
					} else if (map[r][c] == '>') {
						coord[0] = r;
						coord[1] = c;
						coord[2] = 3;
					}
				}
			}
			
//			System.out.println(Arrays.toString(coord));
			
			
			int N = Integer.parseInt(br.readLine());
			char[] OP = br.readLine().toCharArray();
			
			for (int i=0; i<N; i++) {
				
//				System.out.println(Arrays.toString(coord));
				
				int r = coord[0];
				int c = coord[1];
				
				if (OP[i] == 'S') {
					int sr = r;
					int sc = c;
					while (sr<H && sr>=0 && sc<W && sc>=0) {
						if (map[sr][sc] == '#') {
							break;
						} else if (map[sr][sc] == '*') {
							map[sr][sc] = '.';
							break;
						}
						sr += dr[coord[2]];
						sc += dc[coord[2]];
					}
				} else {
					if (OP[i] == 'U') {
						coord[2] = 0;
						map[r][c] = '^';
					} else if (OP[i] == 'D') {
						coord[2] = 1;
						map[r][c] = 'v';
					} else if (OP[i] == 'L') {
						coord[2] = 2;
						map[r][c] = '<';
					} else if (OP[i] == 'R') {
						coord[2] = 3;
						map[r][c] = '>';
					}
					
					int nr = r+dr[coord[2]];
					int nc = c+dc[coord[2]];
					
					if (nr<H && nr>=0 && nc<W && nc>=0 && map[nr][nc] == '.') {				
						coord[0] = nr;
						coord[1] = nc;
						map[nr][nc] = map[r][c];
						map[r][c] = '.';
					}
					
				}
				
			}
			
			sb.append("#").append(t).append(" ");
			
			for (int r=0; r<H; r++) {
				for (int c=0; c<W; c++) {
					sb.append(map[r][c]);
				}
				sb.append("\n");
			}
			
		}
		System.out.println(sb);
		
	}
}
















