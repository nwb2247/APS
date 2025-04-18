import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int TC = Integer.parseInt(br.readLine());
		
		for (int tc=1; tc<=TC; tc++) {
			
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			
			boolean isOn = true;
			for (int i=0; i<N; i++) {
				if ((1<<i & M) != 0) continue;
				isOn = false;
				break;
			}
			
			sb.append("#").append(tc).append(" ");
			if (isOn) {
				sb.append("ON");
			} else {
				sb.append("OFF");
			}
			
			sb.append("\n");
			
		}
		
		System.out.println(sb.toString());
		
	}

}
