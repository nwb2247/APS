import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int L = Integer.parseInt(st.nextToken());
		
		int[] cnt = new int[N];
		cnt[0] = 1;
		
		int sol = 0;
		int curIdx = 0;
		while (true) {
			if (cnt[curIdx] == M) {
				break;
			}
			
			if (cnt[curIdx] % 2 == 0) {
				curIdx = (curIdx+N-L)%N;
				cnt[curIdx]++;
			} else {
				curIdx = (curIdx+N+L)%N;
				cnt[curIdx]++;
			}
			
			sol++;
		}
		
		System.out.println(sol);

	}

}
