import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int L = Integer.parseInt(br.readLine());
		int N = Integer.parseInt(br.readLine());
		
		int expectedCnt = 0;
		int expectedMan = 0;
		
		int[] cakes = new int[L+1];
		int[] realCnts = new int[N+1];
		for(int i=1; i<=N; i++) {
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			
			if (end-start+1>expectedCnt) {
				expectedCnt = end-start+1;
				expectedMan = i;
			}
			
			for (int j=start; j<=end; j++) {
				if (cakes[j] == 0) {
					cakes[j] = i;
					realCnts[i] ++;
				}
			}
		}
		
		int realCnt = 0;
		int realMan = 0;
		for (int i=1; i<=N; i++) {
			if (realCnts[i] > realCnt) {
				realCnt = realCnts[i];
				realMan = i;
			}
		}
		
		System.out.println(expectedMan);
		System.out.println(realMan);
//		System.out.println(Arrays.toString(cakes));
//		System.out.println(Arrays.toString(realCnts));

	}

}
