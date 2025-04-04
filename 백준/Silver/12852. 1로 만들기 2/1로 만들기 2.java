import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int X = Integer.parseInt(br.readLine());
		
		int[] DP = new int[X+1];
		Arrays.fill(DP, Integer.MAX_VALUE);
		DP[1] = 0;
		
		int[] prev = new int[X+1];
		
		for (int i=1; i<=X; i++) {
			if (i*3 <= X && DP[i]+1 < DP[i*3]) {
				DP[i*3] = DP[i]+1;
				prev[i*3] = i;
			}
			if (i*2 <= X && DP[i]+1 < DP[i*2]) {
				DP[i*2] = DP[i]+1;
				prev[i*2] = i;
			}
			if (i+1 <= X && DP[i]+1 < DP[i+1]) {
				DP[i+1] = DP[i]+1;
				prev[i+1] = i;
			}
		}
		
//		System.out.println(Arrays.toString(DP));
		sb.append(DP[X]).append("\n");
		int cur = X;
		while (cur != 0) {
			sb.append(cur).append(" ");
			cur = prev[cur];
		}
		
		System.out.println(sb.toString());
		

	}

}
