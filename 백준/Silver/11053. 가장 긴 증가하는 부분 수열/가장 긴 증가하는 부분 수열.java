import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	// BJ11053 가장 긴 증가하는 부분수열
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		int[] arr = new int[N];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for (int i=0; i<N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		int[] len = new int[N];
		len[N-1] = 1;
		
		int max = 1;
		for (int i=N-2; i>=0; i--) {
			
			int curLen = 0;
			for (int j=i+1; j<N; j++) {
				if (arr[j] > arr[i]) {
					curLen = Math.max(curLen, len[j]);
					
				}
			}
			
			len[i] = 1 + curLen;
			max = Math.max(max, len[i]);
			
		}
//		System.out.println(Arrays.toString(len));
		System.out.println(max);
		

	}

}
