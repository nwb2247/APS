import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		int[] score = new int[N+1];
		int[][] DP = new int[N+1][3]; 
		// [i][0] : i o i-1 x i-2 o
		// [i][1] : i o i-1 o i-2 x
		// [i][2] : i x i-1 o i-2 x/o
		
		for (int i=1; i<=N; i++) {
			score[i] = Integer.parseInt(br.readLine());
		}
		
		DP[1][0]= score[1];
		DP[1][1]= score[1];
		for (int i=2; i<=N; i++) {
			DP[i][0] = DP[i-1][2]+score[i];
			DP[i][1] = DP[i-1][0]+score[i];
			DP[i][2] = Math.max(DP[i-1][0], DP[i-1][1]);
		}
		
		System.out.println(Math.max(DP[N][0], DP[N][1])); // 마지막 계단은 반드시 밟아야하므로 DP[N][2]는 고려 X
//		System.out.println(Arrays.toString(score));
//		System.out.println(Arrays.deepToString(DP));
	}

}
