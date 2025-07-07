import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int r = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());
		
		int cur = (int) Math.pow(2, N);
		int sol = 0;
		for (int i=1; i<=N; i++) {
			cur /= 2;
			int q = 0;
			if (cur<=c) {
				q += 1;
				c -= cur;
			}
			if (cur<=r) {
				q += 2;
				r -= cur;
			}
			sol += q*cur*cur;
		}
		
		System.out.println(sol);	
		
		
	}
}