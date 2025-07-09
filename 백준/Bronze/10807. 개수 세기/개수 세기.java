import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int[] cnt = new int[201];
		int N = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		for (int i=0; i<N; i++) {
			cnt[Integer.parseInt(st.nextToken())+100]++;
		}
		
		System.out.println(cnt[Integer.parseInt(br.readLine())+100]);
	}
	
	
}