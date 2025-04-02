import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws IOException {
		
		// 카운팅 정렬은 특별한 조건에서만 사용가능
		// 모든 요소가 정수형(빈도수 체크가 가능해야하므로)
		// 범위가 알려져있거나, 작아야함 (안그러면 메모리를 너무 많이 사용함)
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int M = 100; // 가로 길이
		
		for (int t=1; t<=10; t++) {
			int N = Integer.parseInt(br.readLine());
			
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			int[] arr = new int[M]; //
			int[] cnt = new int[101]; // 범위 1~100이지만 편의상 101개로
 			for (int i=0; i<M; i++) {
 				int num = Integer.parseInt(st.nextToken());
 				arr[i] = num;
 				cnt[num]++;
 			}
 			
 			for (int i=1; i<101; i++) {
 				cnt[i] += cnt[i-1];
 			}
 			
 			int[] sortArr =new int[M];
 			for (int i=M-1; i>=0; i--) { // 안정정렬을 위한 역순 순회
 				sortArr[--cnt[arr[i]]] = arr[i];
 			}
 			
// 			System.out.println(Arrays.toString(sortArr)); // 정렬되었는지 확인
 			
 			
 			
 			// 덤프 시작
 			int gap = sortArr[M-1] - sortArr[0];
 			
 			for (int n=0; n<N; n++) {			
 				if (gap <= 1) {
 					break;
 				}
 				
 				sortArr[M-1]--;
 				sortArr[0]++;
 				
 				for (int i=1; i<M; i++) {
 					if (sortArr[i] < sortArr[i-1]) {
 						// swap
 						int temp = sortArr[i];
 						sortArr[i] = sortArr[i-1];
 						sortArr[i-1] = temp;
 					} else {
 						break;
 					}
 				}
 				
 				for (int i=M-2; i>=0; i--) {
 					if (sortArr[i] > sortArr[i+1]) {
 						//swap
 						int temp = sortArr[i];
 						sortArr[i] = sortArr[i+1];
 						sortArr[i+1] = temp;
 					} else {
 						break;
 					}
 				}
 				gap = sortArr[M-1] - sortArr[0];
 			}
 			
// 			System.out.println(Arrays.toString(sortArr));
 			System.out.println("#" + t + " " + gap);
 			
		}

	}

}
