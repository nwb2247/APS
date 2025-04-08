import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		// 최장증가부분수열 LIS (longest increasing subsequence)
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[N];
		
		st = new StringTokenizer(br.readLine());
		for (int i=0; i<N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());				
		}
		
		/*
		 * C[len] : 	길이가 len인 증가부분수열들 중에서 
		 * 				"가장 큰 숫자(즉 (len-1)번째 숫자)"가 최소인 부분수열의 "가장 큰 숫자"
		 * => 갱신 방법 : 새로운 숫자 n에 대해 C내부에서 binary search를 통해
		 * 				n보다 큰 것중 가장 작은 C[i]를 찾고, C[i]=n으로 갱신해줌 	
		 */
		int[] C = new int[N];
		
		int size = 0;
		
		for (int i=0; i<N; i++) {
			int pos = Arrays.binarySearch(C, 0, size, arr[i]);
			/*
			 * index of the search key, if it is contained in the arraywithin the specified range;
			 * otherwise, (-(insertion point) - 1). 
			 * The insertion point is defined as the point at which thekey would be inserted into the array: 
			 * the index of the first element in the range greater than the key
			 * 
			 * C[0]~C[size] 까지에서 arr[i]를 찾음
			 * => 못찾으면 -insertion point - 1을 반환 (인덱스가 0인경우 0이아닌 -1이 반환되기 위해 설계)
			 */
			if (pos>=0) continue; // 찾는 값이 있다 -> 중복이 있다는 의미!
			
			int len = Math.abs(pos)-1;
			C[len] = arr[i];
			if(len == size) ++size;
		}
		
//		System.out.println(Arrays.toString(C));
		System.out.println(size);
		
		
		

	}

}
