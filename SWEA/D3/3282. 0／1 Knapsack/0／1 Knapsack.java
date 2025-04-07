import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		
		for (int t=1; t<=T; t++) {
			
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int K = Integer.parseInt(st.nextToken());
			
			int[] cMax = new int[K+1]; // cMax[v] : 부피 v이하에서 얻을 수 있는 최대 가치(c)
			
			for (int i=0; i<N; i++) {
				st = new StringTokenizer(br.readLine());
				int v = Integer.parseInt(st.nextToken());
				int c = Integer.parseInt(st.nextToken());
				
				for (int j=K; j>=v; j--) {
					cMax[j] = Math.max(cMax[j], cMax[j-v]+c);
				}
			}
			
			sb.append("#").append(t).append(" ").append(cMax[K]).append("\n");

		}
		
		System.out.println(sb.toString());
		
		

	}

}
