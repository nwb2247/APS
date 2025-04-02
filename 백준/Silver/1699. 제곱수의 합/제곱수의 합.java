import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	
	//BJ1699  제곱수의 합

	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		int[] cnt = new int[N+1];
		
		for (int i=1; i<=N; i++) {
			cnt[i] = i;
			for (int j=1; j*j <=i; j++) {
				cnt[i] = Math.min(cnt[i], cnt[i-j*j] + 1); // 1은 j*j를 의미
			}
		}
//		System.out.println(Arrays.toString(cnt));
		System.out.println(cnt[N]);
 		
		
	}

}
