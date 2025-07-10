import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		char[] chars = br.readLine().toCharArray();
		int sum = 0;
		for (char c : chars) {
			if (c >= 'W') {
				sum += 10;
			} else if (c >= 'T') {
				sum += 9;
			} else if (c >= 'P') {
				sum += 8;
			} else if (c >= 'M') {
				sum += 7;
			} else if (c >= 'J') {
				sum += 6;
			} else if (c >= 'G') {
				sum += 5;
			} else if (c >= 'D') {
				sum += 4;
			} else if (c >= 'A') {
				sum += 3;
			}
		}
		System.out.println(sum);

	}
}