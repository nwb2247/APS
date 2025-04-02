import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	// BJ11057 오르막수
 	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
 		
 		int div = 10007;
 		
 		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 		
 		int N = Integer.parseInt(br.readLine());
 		
 		br.close();
 		
 		int[][] DP = new int[N+1][10];
 		
 		for (int i=0; i<10; i++) {
 			DP[1][i] = 1;
 		}
 		
 		for (int i=2; i<=N; i++) {
 			for (int j=0; j<10; j++) {
 				for (int k=0; k<=j; k++) {
 					DP[i][j] = (DP[i][j] + DP[i-1][k]%div)%div;
 				}
 			}
 		}
 		
 		int sum = 0;
 		for (int i=0; i<10; i++) {
 			sum = (sum + DP[N][i]%div)%div;
 		}
 		
 		System.out.println(sum);
 		

	}

}
