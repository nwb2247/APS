import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int[] pos = new int[26];
		Arrays.fill(pos, -1);
		char[] chars = br.readLine().toCharArray();
		for (int i=0; i<chars.length; i++) {
			if (pos[chars[i]-'a'] == -1) pos[chars[i]-'a'] = i; 
		}
		for (int i=0; i<26; i++) {
			sb.append(pos[i]).append(" ");
		}
		System.out.println(sb.toString());
		

	}
}