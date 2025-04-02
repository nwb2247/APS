import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	// BJ2810
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		char[] arr = br.readLine().toCharArray();
		
		int cnt = 1; // 맨 왼쪽
		
		int i=0;
		while (i<N) {
			if (arr[i] == 'S') {
				i++;
			} else { //'L'
				i += 2;
			}
			cnt++;
		}
		
		System.out.println(Math.min(cnt, N));
	}

}
