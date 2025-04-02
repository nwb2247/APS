import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	
	// BJ11727

	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		if (N == 1) {
			System.out.println(1);
			return;
		}
		
		int[] dp = new int[N+1];
		
		dp[0] = 1;
		dp[1] = 1;
		dp[2] = 3;
		
		for (int i=3; i<=N; i++) {
			dp[i] = 1; // 모든 타일이 세로타일인 경우
			
			// 가로 타일 혹은 정사각 타일의 첫 등장 이후 나머지 i-2개의 타일의 배치는 dp에서 참조함
			for (int j=0; j<=i-2; j++) {
				dp[i] = (dp[i] + 2*dp[j]) % 10007;
			}
		}
		
		System.out.println(dp[N]);

	}

}
