import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	// BJ1309 동물원

	public static void main(String[] args) throws IOException {
		
		int div = 9901;
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		// 사자 최대 N마리
		int[][] DP = new int[N+1][2]; // 1 : 왼쪽 or 오른쪽에 사자 존재 (왼/오 한 경우만을 고려) 0 : 없음
		
		DP[1][0] = 1;
		DP[1][1] = 1;
				
		for (int i=2; i<=N; i++) {
			DP[i][0] = (DP[i-1][0]%div + 2*DP[i-1][1]%div)%div ; // 왼/오 이므로 곱하기 2
			DP[i][1] = (DP[i-1][0]%div + DP[i-1][1]%div)%div;
		}
 		
		System.out.println((DP[N][0]%div + 2*DP[N][1]%div)%div);
		
	}
	
}
