import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
	
	static int N, B;
	static int[] height;	
	static int min;

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		
		for (int t=1; t<=T; t++) {
			
			st = new StringTokenizer(br.readLine());
			
			N = Integer.parseInt(st.nextToken());
			B = Integer.parseInt(st.nextToken());
			height = new int[N];
			
			st = new StringTokenizer(br.readLine());
			for (int i=0; i<N; i++) {
				height[i] = Integer.parseInt(st.nextToken());
			}
			
//			System.out.println(Arrays.toString(height));
			min = Integer.MAX_VALUE;
			
			makeComb(0, 0);
			sb.append("#"+t+" "+min+"\n");

		}
		
		System.out.println(sb);

	}
	
	private static void makeComb(int startIdx, int sum) {
		
		if (sum-B >= 0) {
			if (sum-B >= min) {
				return;
			} else {
				min = Math.min(min, sum-B);
			}
		}
		
		for (int i=startIdx; i<N; i++) {
			makeComb(i+1, sum+height[i]);
		}
			
	}

}
