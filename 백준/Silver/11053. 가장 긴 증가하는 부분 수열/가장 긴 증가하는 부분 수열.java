import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[N];
		st = new StringTokenizer(br.readLine());
		for (int i=0; i<N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		int[] minLast = new int[N];
		// minLast[len-1] : 증가부분수열의 길이가 len인 것중 마지막(가장큰)숫자가 가장 작은 것
		// => 갱신 방법 : 새로운 숫자 n에 대해 C내부에서 binary search를 통해
		// n보다 큰 것중 가장 작은 C[i]를 찾고, C[i]=n으로 갱신해줌 	
		int maxLen = 0;
		for (int i=0; i<N; i++) {
			int pos = Arrays.binarySearch(minLast, 0, maxLen, arr[i]);
			/*
			 * Arrays.binarySearch(minLast, 0, maxLen, arr[i])
			 * 존재하면 			=> 해당 인덱스, 
			 * 존재하지 않으면 		=> -삽입될인덱스-1를 (0일 경우 -1을 반환하도록 하기 위해)
			 * 반환함
			 */
			if (pos >= 0) continue;
			int idx = -pos-1;
			minLast[idx] = arr[i];
			maxLen = Math.max(maxLen, idx+1); // idx==len-1이므로 len==idx+1, 갱신 필요하다면 갱신
		}
		
		System.out.println(maxLen);
		
		

	}

}
