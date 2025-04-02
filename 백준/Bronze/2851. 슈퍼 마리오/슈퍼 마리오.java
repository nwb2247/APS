import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int[] cumsum = new int[10+1];
		
		int i=1;
		while(true) {
			cumsum[i] = cumsum[i-1] + Integer.parseInt(br.readLine());
			if (cumsum[i] >= 100 || i==10) {
				break;
			}
			i++;
			
		}
		
		int diffPrev = 100-cumsum[i-1];
		int diff = (cumsum[i] > 100) ? cumsum[i]-100 : 100-cumsum[i];
		
		int sol = 0;
		if (diffPrev < diff) {
			sol = cumsum[i-1];
		} else {
			sol = cumsum[i];
		}
		
		System.out.println(sol);
		
	}

}
