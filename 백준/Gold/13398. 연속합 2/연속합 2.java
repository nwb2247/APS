import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[N];
		int[] cumSum = new int[N]; // cumSum[i] 0~i-1까지의 누적합 (단, cumSum[0]은 의미없는 수 )
		int[] cumSumRev = new int[N]; // cumSumRev[i] i+1~n-1까지의 누적합 (단, cumSumRev[n-1]은 의미없는 수)
		
		// cumSum[0] cumSumRev[0] 는 누적합이 아닌데, N == 1이면 누적합인 것처럼 계산되므로 문제가 발생
		// 반례
		// 1
		// -10
		// 올바른 답 : -10; 아래 예외조건이 없으면 0을 반환함
		if (N == 1) {
			System.out.println(Integer.parseInt(br.readLine()));
			return;
		}
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for (int i=0; i<N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		for (int i=1; i<N; i++) {
			cumSum[i] = Math.max(cumSum[i-1] + arr[i-1], arr[i-1]);
		}
		
		for (int i=N-2; i>=0; i--) {
			cumSumRev[i] = Math.max(cumSumRev[i+1] + arr[i+1], arr[i+1]);
		}
		
//		System.out.println(Arrays.toString(cumSum));
//		System.out.println(Arrays.toString(cumSumRev)); 

		int max = Integer.MIN_VALUE;
		for (int i=0; i<N; i++) {
			max = Math.max(max, arr[i]);
			max = Math.max(max, cumSum[i] + arr[i] + cumSumRev[i]);
			max = Math.max(max, cumSum[i] + arr[i]);
			max = Math.max(max, arr[i] + cumSumRev[i]);
			max = Math.max(max, cumSum[i] + cumSumRev[i]);
		}

		System.out.println(max);
				

	}

}
