import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
		for (int t=1; t<=T; t++) {
			int N = Integer.parseInt(br.readLine());
			int[][] map = new int[N][N];
			
			int K = N; // 같은 방향으로 연달아 몇번 입력할 것인지
			int dir = 1; // 해당 방향에 대한 증감을 의미
			
			int r=0, c=-1;
			int num = 1; 
			while (K >= 0) { // 다른 여러 종료 조건도 가능 (num <= N*N-1 등)
				
				for (int k=1; k<=K; k++) { // k는 현재방향에서 더해진 횟수를 의미
					c += dir;
					map[r][c] = num++;
				}
				
				K--;
				
				for (int k=1; k<=K; k++) {
					r += dir;
					map[r][c] = num++;
				}
				
				dir = -dir;
			}
			
			StringBuilder sb;
			System.out.println("#"+t);
			
			for (r=0; r<N; r++) {
				sb = new StringBuilder();
				for (c=0; c<N; c++) {
					sb.append(map[r][c] + " ");
				}
				System.out.println(sb.toString());
			}
			
		}

	}

}
