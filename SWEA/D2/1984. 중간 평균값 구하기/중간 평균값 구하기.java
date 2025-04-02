import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		for (int t=1; t<=T; t++) {
			
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			int min = Integer.MAX_VALUE;
			int max = 0;
			int sum = 0;
			for (int i=0; i<10; i++) {
				int e = Integer.parseInt(st.nextToken());
				min = Math.min(min, e);
				max = Math.max(max, e);
				sum += e;
			}
			sum -= (min + max);
			System.out.println("#" + t + " "+ Math.round(((double) sum)/8));

		}

	}

}
