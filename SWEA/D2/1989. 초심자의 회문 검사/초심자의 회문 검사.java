import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		for (int t=1; t<=T; t++) {
			String str = br.readLine();
			int len = str.length();
			
			int sol = 1;
			for (int i=0; i<len/2; i++) {
				if (str.charAt(i) != str.charAt(len - 1 - i)) {
					sol = 0;
					break;
				}
			}
			
			System.out.println("#"+t+" "+sol);
			
		}
		

	}

}
