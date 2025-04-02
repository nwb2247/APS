import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int N;
	static int[] arr;

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		N = Integer.parseInt(br.readLine());
		arr = new int[N];
		st = new StringTokenizer(br.readLine());
		for (int i=0; i<N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(arr);
		
//		System.out.println(Arrays.toString(arr));
		
		int M = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		for (int i=0; i<M; i++) {
			sb.append(binarySearch(Integer.parseInt(st.nextToken()))+"\n");					// while 버전
//			sb.append(binarySearch(Integer.parseInt(st.nextToken()), 0, N-1)+"\n");		// 재귀 버전
		}
		
		System.out.println(sb);
		
		

	}
	
	static int binarySearch(int val) {
		
		int left = 0;
		int right = N-1;
		int mid = -1;
		
		while (left<=right) {
			
			mid = (left+right)/2;
			
			if (val < arr[mid]) {
				right = mid-1;
			} else  if (val > arr[mid]) {
				left = mid+1;
			} else {
				return 1;
			}
			
		}

		return 0;
	}
	
	
	
	
//	재귀버전
//	이분탐색은 재귀가 코드는 쉽지만 성능 측면에서 while문이 더 뛰어남 (스택을 쌓지 않으므로)
//	static int binarySearch(int val, int left, int right) { 
//		
//		if (right < left) {
//			return 0;
//		}
//		
//		int mid = (left+right)/2;
//		
////		System.out.println("val: " + val + " mid: " + arr[mid]);
//		
//		if (val < arr[mid]) {
//			return binarySearch(val, left, mid-1);
//		} else if (val > arr[mid]) {
//			return binarySearch(val, mid+1, right);
//		} else { // val == mid
//			return 1;
//		}
//			
//	}

}
