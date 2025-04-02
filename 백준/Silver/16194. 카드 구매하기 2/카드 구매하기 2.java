import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	//BJ16194 카드구매하기2
	
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		int[] dp = new int[N+1];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		
		// BJ11052 카드구매하기 참고
		for (int i=1; i<=N; i++) {
			dp[i] = Integer.parseInt(st.nextToken());
			
			for (int j=0; j<=i/2; j++) {
				dp[i] = Math.min(dp[i], dp[i-j] + dp[j]);
			}
		}
		
		System.out.println(dp[N]);

	}

}
