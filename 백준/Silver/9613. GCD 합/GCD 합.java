import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		StringBuilder sb = new StringBuilder();
		
		for (int t=1; t<=T; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			int N = Integer.parseInt(st.nextToken());
			int[] nums = new int[N];
			
			for (int i=0; i<N; i++) {
				nums[i] = Integer.parseInt(st.nextToken());
			}
			
			Arrays.sort(nums); // 정방향 정렬
			// 역순 정렬 위해선 Integer[]로 받아야함		
			
			long count = 0;    				// 합의 범위가 int를 초과할 수 있음
			for (int i=0; i<N-1; i++) {
				for (int j=i+1; j<N; j++) {
					 count += GCD(nums[j], nums[i]);
				}
			}
			
			sb.append(count + "\n");
		}
		
		System.out.println(sb.toString().trim());
		
	}
	
	
	// 유클리드 호제법
	public static int GCD(int A, int B) { // A is bigger
		
		if (A % B == 0) {
			return B;
		} else {
			return GCD(B, A % B);
		}
	}

}
