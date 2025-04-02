import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	// BJ8958 OX퀴즈
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		for(int t=1; t<=T; t++) {
			char[] arr = br.readLine().toCharArray();
			
			int seq = 0;
			int sum = 0;
			for(int i=0; i<arr.length; i++) {
				if (arr[i] == 'O') {
					seq++;
					sum += seq;
				} else { // 'X'
					seq = 0;
				}
			}
			
			System.out.println(sum);
		}
		
		

	}

}
