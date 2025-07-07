import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		while (true) {
			
			st = new StringTokenizer(br.readLine());
			int[] len = new int[3];
			len[0] = Integer.parseInt(st.nextToken());
			len[1] = Integer.parseInt(st.nextToken());
			len[2] = Integer.parseInt(st.nextToken());
			
			if (len[0] == 0 && len[1] == 0 && len[2] == 0) break;
			
			Arrays.sort(len);
			
			if (len[0]*len[0] + len[1]*len[1] == len[2]*len[2]) {
				sb.append("right");
			} else {
				sb.append("wrong");
			}
			sb.append("\n");
			
		}
		
		System.out.println(sb.toString());
		
		
	}
}