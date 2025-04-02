import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int N, M;
	static int cnt = 0;
	static int[] output;
	static StringBuilder sb;

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		sb = new StringBuilder();
		output = new int[M];	
		
		comb(0, 1);
		System.out.println(sb);

	}
	
	public static void comb (int cnt, int startIdx) {
		
		if (cnt == M) {
			for (int i=0; i<M; i++) {
				sb.append(output[i] + " ");
			}
			sb.append("\n");
			return;
		}
		
		for (int i=startIdx; i<=N; i++) {
			
			output[cnt] = i;
			comb(cnt+1, i+1);
			
		}
		
	}

}
