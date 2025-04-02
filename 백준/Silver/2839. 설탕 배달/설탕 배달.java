import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	static int N;

	public static void main(String[] args) throws IOException {
		
		init();
		solve();

	}
	
	static void solve() {
		
		int five = N / 5;
		
		int sol = -1;
		while (five >= 0) {
			if ((N-five*5) % 3 == 0) {
				sol = five + (N-five*5)/3;
				break;
			}
			five--;
			
		}
		
		System.out.println(sol);
		
	}
	
 	
	static void init() throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		
		br.close();
	}

}
