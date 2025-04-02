import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		int[] arr = new int[N];
		int[] asc = new int[N];
		int[] desc = new int[N];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for (int i=0; i<N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		for (int i=0; i<N; i++) {
			for (int j=0; j<i; j++) {
				if (arr[j] < arr[i]) {
					asc[i] = Math.max(asc[i], asc[j]);
				}
			}
			asc[i] += 1;
		}
		
		for (int i=N-1; i>=0; i--) {
			for (int j=N-1; j>i; j--) {
				if (arr[j] < arr[i]) {
					desc[i] = Math.max(desc[i], desc[j]);
				}
			}
			desc[i] += 1;
		}
		
		int max = 0;
		for (int i=0; i<N; i++) {
			max = Math.max(max, asc[i] + desc[i] - 1); // 꺾이는 지점의 수가 두번 체크되므로 1을 뺌
		}
		
		System.out.println(max);

		

	}

}
