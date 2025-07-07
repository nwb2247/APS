import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int C = Integer.parseInt(st.nextToken());
		int N = Integer.parseInt(st.nextToken());
		
		int[] cost = new int[N];
		int[] num = new int[N];
		
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			cost[i] = Integer.parseInt(st.nextToken()); // 비용
			num[i] = Integer.parseInt(st.nextToken());	// 사람 수
		}
		
		int[] min = new int[C+1];
		for (int i=0; i<N; i++) {
			Arrays.fill(min, Integer.MAX_VALUE);
		}
		
		for (int i=0; i<N; i++) {
			for (int j=0; j*num[i]<=C; j++) {
				min[j*num[i]] = Math.min(min[j*num[i]],j*cost[i]);
			}
		}
		
//		System.out.println(Arrays.toString(min));	
		
		for (int i=1; i<=C; i++) {
			for (int j=0; j<N; j++) {
				if (i-num[j] < 0) continue;
				if (min[i-num[j]] == Integer.MAX_VALUE) continue;
				min[i] = Math.min(min[i], Math.max(0,min[i-num[j]]+cost[j]));
			}
		}
		
//		System.out.println(Arrays.toString(min));
		
		for (int i=0; i<N; i++) {
			int m = Integer.MAX_VALUE;
			for (int j=Math.max(0, C-num[i]); j<C; j++) {
				m = Math.min(m, min[j]);
			}
			min[C] = Math.min(min[C], m+cost[i]);
		}
		
		System.out.println(min[C]);

	}

}
