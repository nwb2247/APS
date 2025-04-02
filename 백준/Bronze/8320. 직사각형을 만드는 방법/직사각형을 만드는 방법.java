import java.io.*;
import java.util.*;

class Main {

	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());		
		
		int count = 0;
		for(int i=1; i<=N; i++) {
			inner:
			for(int j=i; j<=N; j++) {
				if (i*j <= N) {
					count++;
				} else if (i*j > N) {
					break inner;
				}
			}
		}
		
		System.out.println(count);
		
	}
}
