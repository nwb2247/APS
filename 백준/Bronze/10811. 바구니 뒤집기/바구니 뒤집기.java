import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		int[] basket = new int[N+1];
		for (int i=1; i<=N; i++) {
			basket[i] = i;
		}
		
 		for (int m=0; m<M; m++) {
			st = new StringTokenizer(br.readLine());
			int i = Integer.parseInt(st.nextToken());
			int j = Integer.parseInt(st.nextToken());
			for (int s=0; s<=(i+j)/2-i; s++) {
				int temp = basket[i+s];
				basket[i+s] = basket[j-s];
				basket[j-s] = temp;
			}
		}
 		
 		for (int i=1; i<=N; i++) {
 			sb.append(basket[i]).append(" ");
 		}

 		
 		System.out.println(sb.toString());
		
	}
}