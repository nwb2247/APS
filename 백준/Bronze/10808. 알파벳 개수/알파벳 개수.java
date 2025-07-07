import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args)  throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		char[] chars = br.readLine().toCharArray();
		
		int[] count = new int[26];
		
		for (char c : chars) {
			count[c-'a']++;
		}
		
		for (int i : count) {
			sb.append(i + " ");
		}
		
		System.out.println(sb.toString());		

	}

}
