import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	// BJ11399
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int[] cnt = new int[1000+1]; // 범위 1~1000
		int[] origin = new int[N];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		// 카운트 정렬
		for (int i=0; i<N; i++) {
			origin[i] = Integer.parseInt(st.nextToken());
			cnt[origin[i]]++;
		}
		
		for (int i=1; i<=1000; i++) {
			cnt[i] += cnt[i-1];
		}
		
		int[] sorted = new int[N]; 
		for (int i=N-1; i>=0; i--) {
			sorted[--cnt[origin[i]]] = origin[i];
		}
		
//		System.out.println(Arrays.toString(sorted));
		
		int sol = sorted[0];
		for (int i=1; i<N; i++) {
			sorted[i] += sorted[i-1];
			sol += sorted[i];
		}
		
		System.out.println(sol);
		

	}

}
