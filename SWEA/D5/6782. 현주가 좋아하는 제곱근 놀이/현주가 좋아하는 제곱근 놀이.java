import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		
		for (int t=1; t<=T; t++) {

			long N = Long.parseLong(br.readLine());
			
			long cnt = 0;
			while(N!=2) {
				
				long sqrt = (long) Math.sqrt(N);
				if (sqrt*sqrt == N) { 
					cnt++;
					N = sqrt;
				} else {
					cnt += (sqrt+1)*(sqrt+1)-N;
					N = (sqrt+1)*(sqrt+1);
					
				}			
				
			}
			
			sb.append("#").append(t).append(" ").append(cnt).append("\n");

			
		}
		
		System.out.println(sb);

	}


}
