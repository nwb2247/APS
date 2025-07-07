import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		
		int[] nums = new int[N];
		boolean[] isIn = new boolean[2000001];
		
		st = new StringTokenizer(br.readLine());
		
		for (int i=0; i<N; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
			isIn[nums[i]] = true;
		}
		
		int X = Integer.parseInt(br.readLine());
		
		int cnt = 0;
		
		for (int num : nums) {
			if (X-num >=1 && isIn[X-num]) {
				cnt++;
			}	
		}
		
		System.out.println(cnt/2);
		

	}

}
