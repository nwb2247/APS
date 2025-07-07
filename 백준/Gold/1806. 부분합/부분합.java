import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int S = Integer.parseInt(st.nextToken());
		
		int[] arr = new int[N];
		st = new StringTokenizer(br.readLine());
		for (int i=0; i<N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		int min = Integer.MAX_VALUE;
		int sum = 0;
		int head = 0;
		for (int i=0; i<N; i++) {
			sum += arr[i];
			if (sum < S) continue;
			while (head<N && sum-arr[head]>=S) {
				sum -= arr[head];
				head++;
			}
//			System.out.println(head + " " + i);
			min = Math.min(min, i-head+1);
		}
		if (sum >= S) {
			System.out.println(min);
		} else {
			System.out.println(0);
		}
	}
	
}
