import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int sum = 0;
		char[] chars = br.readLine().toCharArray();
		for (int i=0; i<N; i++) {
			sum += chars[i] - '0';
		}
		System.out.println(sum);

	}
}