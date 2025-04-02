import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		if (N%2 == 1) {
			System.out.println(0);
			return;
		}
		
		int[][] DP = new int[N/2+1][3];
		DP[1][0] = 1; 	// 위만 -
		DP[1][1] = 1;	// 아래만 -
		DP[1][2] = 1;	// 셋다 -
		
		for (int i=2; i<=N/2; i++) {
			DP[i][0] = DP[i-1][0]*2 + DP[i-1][1] + DP[i-1][2];
			DP[i][1] = DP[i-1][0] + DP[i-1][1]*2 + DP[i-1][2];
			DP[i][2] = DP[i-1][0] + DP[i-1][1] + DP[i-1][2];
		}
		
		
		System.out.println(DP[N/2][0] + DP[N/2][1] + DP[N/2][2]);

	}

}
