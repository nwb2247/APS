import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int B = Integer.parseInt(st.nextToken());
		
		int A = 'A';
		
		int Q = N;
		int R;
		
		StringBuilder sb = new StringBuilder();
		while (true) {
			
			R = Q%B;
			Q = Q/B;
			if (R < 10) {
				sb.append(Integer.toString(R));
			} else {
				sb.append((char) (R-10+A));
			}
			
			if (Q==0) {
				break;
			}			
			
		}
		
		System.out.println(sb.reverse());
		
		
	}

}
