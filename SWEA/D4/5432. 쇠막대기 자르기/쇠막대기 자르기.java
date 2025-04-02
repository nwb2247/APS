import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Solution {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		for (int t=1; t<=T; t++) {
			char[] arr = br.readLine().toCharArray();
			
			int sum = 0;
			int curNum = 0;
			boolean wasOpen = true;
			for (int i=0; i<arr.length; i++) {
				if (arr[i] == '(') {
					curNum++;
					wasOpen = true;
				} else { // ')'
					if (wasOpen) {
						sum += --curNum;
					} else {
						curNum--;
						sum++;
					}
					wasOpen = false;
				}
			}
			
			System.out.println("#"+t+ " "+ sum);
		}

	}

}
