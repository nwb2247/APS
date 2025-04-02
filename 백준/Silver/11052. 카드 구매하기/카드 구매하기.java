import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	// BJ11052
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		int[] dp = new int[N+1]; 
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for (int i=1; i<=N; i++) {
			dp[i] = Integer.parseInt(st.nextToken());
		}
		
		// dp[0]은 0인 상태
		// i개를 만들수 있는 가장 큰 비용으로 i=1부터 계산해줌
		for (int i=1; i<=N; i++) {
			for (int j=0; j<=i/2; j++) { 
				dp[i] = Math.max(dp[i], dp[i-j] + dp[j]);
			}
			
		}
		
		System.out.println(dp[N]);
		
		
		

	}

}
