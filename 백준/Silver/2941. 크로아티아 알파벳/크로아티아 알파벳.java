import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		char[] chars = br.readLine().toCharArray();
		
		int cnt = 0;
		int i = 0;
		while (i < chars.length) {
			cnt++;
			if (chars[i] == 'c' && 
				i+1 < chars.length && 
				(chars[i+1] == '=' || chars[i+1] == '-')) {
				i+=2;
			} else if ((chars[i] == 's' || chars[i] == 'z') &&
					i+1 < chars.length &&
					chars[i+1] == '=') {
				i+=2;
				
			} else if ((chars[i] == 'l' || chars[i] == 'n') &&
					i+1 < chars.length &&
					chars[i+1] == 'j') {
				i+=2;
			} else if (chars[i] == 'd' && 
					i+1 < chars.length && 
					(chars[i+1] == '-')) {
				i+=2;
			} else if (chars[i] == 'd' && 
					i+1 < chars.length && 
					(chars[i+1] == 'z') &&
					i+2 < chars.length &&
					(chars[i+2] == '=')) {
				i+=3;
			} else {
				i++;
			}
 		}
		System.out.println(cnt);

	}
}