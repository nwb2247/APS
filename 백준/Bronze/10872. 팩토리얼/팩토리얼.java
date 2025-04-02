import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		int sol = 1;
		
		while (N > 0) {
			sol = sol*N;
			N--;
		}
		
		System.out.println(sol);
		
		
				
	}

}
