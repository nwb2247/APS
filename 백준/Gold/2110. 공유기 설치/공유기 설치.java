import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Main {
	
	static int N, C;
	static int[] arr;

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		
		arr= new int[N];
		for (int i=0; i<N; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
		
		Arrays.sort(arr);

		int sol = 1;
		int left = 1;
		int right = arr[N-1] - arr[0];
		while (left<=right) {

			
			int mid = (left+right)/2;
//			System.out.println("l:" + left + " r:" + right + " m:" + mid + " " + check(mid));
			
			if (check(mid)) {
				sol = mid;
				left = mid+1;
			} else {
				right = mid-1;
			}
			
		}
		
		System.out.println(sol);		
		
	}
	
	static boolean check(int dist) {
		
		int i = 0;
		int j = 1;
		int cnt = 1;
		while (i <= N-2 && j <= N-1) {
//			System.out.println(arr[i]+ " " + arr[j] + "  cnt : " + cnt);
			if (arr[j] - arr[i] < dist) {
				j++;
			} else {
				i=j;
				j = i+1;
				cnt++;
			}
			
			if (cnt == C) {
				return true;
			}
		}
		
		return false;
		
	}

}
