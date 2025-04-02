// BJ1929

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] input = br.readLine().split(" ");
		
		int M = Integer.parseInt(input[0]);
		int N = Integer.parseInt(input[1]);
		
		boolean[] prime = new boolean[N+1];
		Arrays.fill(prime, true);
		prime[0] = false;
		prime[1] = false;
		for (int i=2; i<=N; i++) {
			if (!prime[i]) continue;
			for (int j=i+i; j<=N; j += i) {
				prime[j] = false;
			}
		}
		
		StringBuilder sb = new StringBuilder();
		
		for (int i=M; i<=N; i++) {
			if (prime[i]) {
				sb.append(i+"\n");
			}
			
		}
		
		System.out.println(sb);
		
	}
}
