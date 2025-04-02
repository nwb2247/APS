import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		StringBuilder sb = new StringBuilder();
		
		for (int n=1; n<=N; n++) {
			sb.append(make123(Integer.parseInt(br.readLine())) + "\n");
		}
		
		System.out.println(sb);
	}
	
	public static int make123(int N) {
		
		if (N == 0) {
			return 0;
		} else if (N == 1) {
			return 1; 	// 1
		} else if (N == 2) {
			return 2; 	// 2 / 1+1
		} else if (N == 3) {
			return 4;	// 3 / 1+2 / 2+1 / 1+1+1 
		} else {
			return make123(N-1) + make123(N-2) + make123(N-3); // N-1 + 1 / N-2 + 2 / N-3 + 3
		}
		
	}

}
