import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		long A = Integer.parseInt(st.nextToken());
		long B = Integer.parseInt(st.nextToken());
		long C = Integer.parseInt(st.nextToken());

		System.out.println(cal(A,B,C)%C);
		
	}
	
	static long cal(long A, long B, long C) {
		
		if (B == 1) {
			return A%C;
		}
		
		long val = cal(A, B/2, C)%C;
		if (B%2 == 0) {
			return (val*val)%C ;
		} else {
			return (((val*val)%C)*A)%C;
		}
		
	}

}
