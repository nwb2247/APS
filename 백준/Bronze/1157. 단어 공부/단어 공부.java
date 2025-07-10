import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		char[] chars = br.readLine().toCharArray();
		
//		System.out.println((int) 'a' + " " + (int) 'A');
		
		int[] cnt = new int[26];
		
		for (char c :  chars) {
			if (c >= 'a') {
				cnt[c-'a']++;
			} else {
				cnt[c-'A']++;
			}
		}
		
		int max = 0;
		int idx = -1;
		for (int i=0; i<26; i++) {
			if (cnt[i] > max) {
				max = cnt[i];
				idx = i;
			} else if (cnt[i] == max) {
				idx = -1;
			}
		}
		
		if (idx == -1) {
			System.out.println('?');
		} else {
			System.out.println(Character.toChars(idx+'A'));
		}

	}
}