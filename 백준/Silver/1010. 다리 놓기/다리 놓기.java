import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		int[][] DP = new int[30][30];
		DP[0][0] = 1;
		
		int T = Integer.parseInt(br.readLine());
		
		int maxM = 0;
		for (int t=0; t<T; t++) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			for (int i=maxM+1; i<=M; i++) {
				DP[i][0] = 1;
				for (int j=1; j<=M; j++) {
					DP[i][j] = DP[i-1][j-1] + DP[i-1][j];
				}	
			}
			maxM = Math.max(maxM, M);
			
			sb.append(DP[M][N]).append("\n");
//			System.out.println(Arrays.deepToString(DP));
		}
		
		System.out.println(sb.toString());
		
		
		
		
		

	}

}
