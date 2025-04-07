import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		StringBuilder sb = new StringBuilder();
		
		long[] P = new long[100+1];
		P[1] = 1;
		P[2] = 1;
		P[3] = 1;
		P[4] = 2;
		P[5] = 2;
		int maxN = 5;
		
		for (int t=0; t<T; t++) {
			int curN = Integer.parseInt(br.readLine());
			for (int n=maxN+1; n<=curN; n++) {
				P[n] = P[n-1]+P[n-5];
			}
			sb.append(P[curN]).append("\n");
			maxN = Math.max(maxN, curN);
		}
		
		System.out.println(sb);
//		System.out.println(Arrays.toString(P));
		
	}

}
