import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		long a = 1000000000;
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		long S = Long.parseLong(st.nextToken());
		
		long[] bros = new long[N];
		
		st = new StringTokenizer(br.readLine());
		
		for (int i=0; i<N; i++) {
			bros[i] = Math.abs(Long.parseLong(st.nextToken()) - S);
		}
		
		
		long curGCD = bros[0]; // 동생이 한명인경우
		for (int i=1; i<N; i++) {
			curGCD = GCD(curGCD, bros[i]);
		}
		
		System.out.println(curGCD);


	}
	
	public static long GCD(long A, long B) { // A is bigger
		if (A % B == 0) {
			return B;
		} else {
			return GCD(B, A % B);
		}
	}

}
