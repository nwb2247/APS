import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));		
		
		int N = Integer.parseInt(br.readLine());
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int[] prime = new int[1001]; 
		Arrays.fill(prime, 1); // 1로 배열 초기화
		prime[0] = 0;
		prime[1] = 0;
		
		for (int i=2; i<=1000; i++) { // 소수는 2부터 count
			if (prime[i] == 0) continue; // 이전 소수의 배수라면 넘어감
			for (int j=i+i; j<=1000; j += i) { // 소수의 배수를 모두 0으로 설정
				prime[j] = 0;
			}
		}

		int count = 0;
		for (int i=0; i<N; i++) {
			count += prime[Integer.parseInt(st.nextToken())];
		}
		
		System.out.println(count);

	}

}
