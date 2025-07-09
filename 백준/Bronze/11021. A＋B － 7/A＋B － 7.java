import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(br.readLine());
		for (int i=1; i<=N; i++) {
			st = new StringTokenizer(br.readLine());
			sb.append("Case #")
				.append(i)
				.append(": ")
				.append(Integer.parseInt(st.nextToken()) + Integer.parseInt(st.nextToken()))
				.append("\n");
		}
		System.out.println(sb.toString());
		
		
		
	}
}