import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		int[][] DP = new int[N+1][]; // 경계값을 0처리하기 위해 원래 피라미드를 0으로 감쌈
		// 실제 맨꼭대기는 [1][1]에서 시작
		
		DP[0] = new int[2];
		for(int i=1; i<=N; i++) {
			DP[i] = new int[i+2]; // 피라미드 형태가 되도록 하나씩 늘려나감
			
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j=1; j<=i; j++) {
				DP[i][j] = Math.max(DP[i-1][j-1], DP[i-1][j]) + Integer.parseInt(st.nextToken());
			}
			
		}
		
		int sol =0; 
		for (int i=1; i<=N; i++) {
			sol = Math.max(sol, DP[N][i]);
		}
		
		System.out.println(sol);
 
	}

}
