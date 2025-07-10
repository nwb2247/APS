import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		char[] chars = br.readLine().toCharArray();
		
		int sol = 1;
		for (int i=0; i<chars.length/2; i++) {
			if (chars[i] != chars[chars.length-1-i]) {
				sol = 0;
				break;
			}
		}
		System.out.println(sol);

	}
}