import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		
		boolean[][] map = new boolean[101][101];
		
		for (int n=1; n<=N; n++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			for (int r=y; r<y+10; r++) {
				for (int c=x; c<x+10; c++) {
					map[r][c] = true;
				}
			}	
		}
		
//		for (int r=0; r<25; r++) {
//			for (int c=0; c<25; c++) {
//				if (map[r][c]) {
//					System.out.print(1+" ");
//				} else {
//					System.out.print(0+" ");
//				}
//				
//			}
//			System.out.println();
//		}
		
		int cnt = 0;
		for (int r=0; r<101; r++) { // 행 방향 순회
			for (int c=1; c<101; c++) { // 이전 것과 비교 위해 c=1부터
				if(map[r][c-1]!=map[r][c]) {
					cnt++;
				}
			}
		}
		for (int c=0; c<101; c++) { // 열 방향 순회
			for (int r=1; r<101; r++) { // 이전 것과 비교 위해 r=1부터
				if(map[r-1][c]!=map[r][c]) {
					cnt++;
				}
			}
		}
		
		System.out.println(cnt);


	}

}
