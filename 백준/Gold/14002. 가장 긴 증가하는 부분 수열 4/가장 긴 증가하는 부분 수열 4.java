import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	// BJ14002 가장 긴 증가하는 부분 수열 4

	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[N];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for (int i=0; i<N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		int[] len = new int[N];
		int[] nextIdx = new int[N];
		
		int maxLen = 1;
		int maxStart = N-1;
		len[N-1] = 1;
		for (int i=N-2; i>=0; i--) {
			int curLen = 0;
			for (int j=i+1; j<N; j++) {
				if (arr[j] > arr[i] && len[j] > curLen) {
					curLen = len[j];
					nextIdx[i] = j;
				}
			}
			len[i] = 1 + curLen;
			
			if (len[i] > maxLen) {
				maxLen = len[i];
				maxStart = i;
			}
		}
		
		StringBuilder sb = new StringBuilder();
		
		int idx = maxStart;
		for (int i=1; i<=maxLen; i++) {
			sb.append(arr[idx] + " ");
			idx = nextIdx[idx];
		}
		
		System.out.println(maxLen);
		System.out.println(sb.toString().trim());

	}

}
