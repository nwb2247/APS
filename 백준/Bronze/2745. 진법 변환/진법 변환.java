import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		String[] arr = st.nextToken().split("");
		
		int B = Integer.parseInt(st.nextToken());
		
		int A = 'A';
		int Z = 'Z';
		
		long N = 0;
		for (String s : arr) {
			long i;
			if (((int) s.charAt(0)) >= A && ((int) s.charAt(0)) <= Z) {
				i = (long) (s.charAt(0) - A + 10);
			} else {
				i = Long.parseLong(s);
			}
			
			N = N*B + i;
			
		}
		
		System.out.println(N);

	}

}
