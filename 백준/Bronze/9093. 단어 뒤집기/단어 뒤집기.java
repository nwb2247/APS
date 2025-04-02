// BJ 9093

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		StringBuilder sb = new StringBuilder();
		
		for (int i=0; i<N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ", true);
			
			while (st.hasMoreTokens()) { // 큐를 이용해도 됨
				char[] chars = st.nextToken().toCharArray(); // 스택을 이용해도 됨
				for (int j = chars.length-1; j>=0; j--) {
					sb.append(chars[j]);
				}
				
			}
			
			sb.append("\n");
			
		}
		
		System.out.println(sb);
		
	}

}
