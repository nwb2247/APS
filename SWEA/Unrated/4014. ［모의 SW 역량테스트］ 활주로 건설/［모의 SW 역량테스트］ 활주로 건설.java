import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int TC = Integer.parseInt(br.readLine());
		
		for (int tc=1; tc<=TC; tc++) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int X = Integer.parseInt(st.nextToken());
			
			int[][] map = new int[N][N];
			
			for (int r=0; r<N; r++) {
				st = new StringTokenizer(br.readLine());
				for (int c=0; c<N; c++) {
					map[r][c] = Integer.parseInt(st.nextToken());
				}
			}
			
			int sol = 0;
			
			outer : 
			for (int r=0; r<N; r++) {
				int h = map[r][0];
				int seq = 0;
				int seqX = X;
				for (int c=0; c<N; c++) {
					if (map[r][c] == h) {
						if (seqX == X) {
							seq++;
						} else {
							seqX++;
						}
					} else if (map[r][c] == h+1) {
						if (seq < X) continue outer;
						h = map[r][c];
						seq = 1;
						seqX = X;
					} else if (map[r][c] == h-1) {
						if (seqX < X) continue outer;
						h = map[r][c];
						seq = 0;
						seqX = 1;
					} else {
						continue outer;
					}
				}
				
				if (seqX<X) continue;
//				System.out.println("r " + r);
				sol++;
				
			}
			
			outer : 
			for (int c=0; c<N; c++) {
				int h = map[0][c];
				int seq = 0;
				int seqX = X;
				for (int r=0; r<N; r++) {
					if (map[r][c] == h) {
						if (seqX == X) {
							seq++;
						} else {
							seqX++;
						}
					} else if (map[r][c] == h+1) {
						if (seq < X) continue outer;
						h = map[r][c];
						seq = 1;
						seqX = X;
					} else if (map[r][c] == h-1) {
						if (seqX < X) continue outer;
						h = map[r][c];
						seq = 0;
						seqX = 1;
					} else {
						continue outer;
					}
				}
				
				if (seqX<X) continue;
//				System.out.println("c " + c);
				sol++;
				
			}
			
			sb.append("#").append(tc).append(" ").append(sol).append("\n");
			
		}
		
		System.out.println(sb);
	}
}
