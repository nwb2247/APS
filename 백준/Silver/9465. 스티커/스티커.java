import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	// BJ9465 스티커

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		StringBuilder sb = new StringBuilder();
		for (int t=1; t<=T; t++) {
			
			int N = Integer.parseInt(br.readLine());
			// 직전까지의 최대값
			
			int[][] map = new int[N][2];
			for (int i=0; i<2; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				for (int j=0; j<N; j++) {
					map[j][i] = Integer.parseInt(st.nextToken());
				}
			}
			
			
			int[][] DP = new int[N][3]; 
			// 마지막으로 선택한 위치
			// 0 위 1 아래 2 아무것도 선택x
			
			 // 맨왼쪽 스티커 무얼 선택할지 초기 설정
			DP[0][0] = map[0][0];
			DP[0][1] = map[0][1];
			
			for (int i=1; i<N; i++) { // 두번째부터
				 
				 for(int j=0; j<3; j++) {
					 DP[i][2] = Math.max(DP[i][2], DP[i-1][j]); 
					 // 아무것도 선택하지 않는다면, 직전에서 최대값을 가져옴
				 }
				 
				 DP[i][0] = Math.max(DP[i-1][2], DP[i-1][1]) + map[i][0];
				 // 위를 선택한다면 직전에서 아무것도 선택하지 않았거나, 아래를 선택한 경우에 더함
				 
				 DP[i][1] = Math.max(DP[i-1][2], DP[i-1][0]) + map[i][1];
				 // 마찬가지
				
			}
			
			int sol = 0;
			for (int i=0; i<3; i++) {
				sol = Math.max(sol, DP[N-1][i]);
			}
			sb.append(sol + "\n");
		
		}

		br.close();
		
		System.out.println(sb);

	}
}
