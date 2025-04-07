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
				int h = map[r][0]; 			// 첫 요소의 높이
				int seq = 0;				// (다음에 낮->높 일 경우를 대비) 다음 경사로 설치를 위해 확보 중인 길이 
				int seqX = X;				// (이전에 높->낮 이었던 경우) 경사로 설치 중인 길이 (처음에는 경사로를 당장 설치할 필요 없으므로 X)
				for (int c=0; c<N; c++) {
					if (map[r][c] == h) {	// 같은 높이가 이어진다면
						if (seqX == X) {		
							seq++;				// 경사로를 다 설치했거나 설치할 필요가 없다면, seq++
						} else {				
							seqX++;				// 경사로가 아직 다 설치되지 않았다면 seqX++
						}
					} else if (map[r][c] == h+1) {
						if (seq < X) continue outer;	// 낮->높 인데 경사로 설치를 위한 길이가 확보되지 않았다면 "불가능"
						h++;							// 높이 갱신
						seq = 1;						
						seqX = X;						// 낮->높이므로 당장 설치할 필요없음
					} else if (map[r][c] == h-1) {
						if (seqX < X) continue outer;	// 높->낮 인데 경사로 설치가 완료되지 않았다면 "불가능"
						h--;				
						seq = 0;						
						seqX = 1;				// 높->낮이므로 곧바로 경사로를 설치해야함. 지금 경사로 설치 완료 되어야 다음 경사로 길이(seq) 확보 가능
					} else {
						continue outer;			// 높이가 2개 이상차이나는경우 "불가능"
					}
				}
				
				if (seqX<X) continue;			// 마지막에 높->낮 이었는데 경사로 설치가 완료되지 않았다면 "불가능"
//				System.out.println("r " + r);
				sol++;							// "불가능" 이 아니라면 카운트
				
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
						h++;
						seq = 1;
						seqX = X;
					} else if (map[r][c] == h-1) {
						if (seqX < X) continue outer;
						h--;
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
