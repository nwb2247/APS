import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken()); // 접시 수
		int d = Integer.parseInt(st.nextToken()); // 가짓수
		int k = Integer.parseInt(st.nextToken()); // 연속 접시 수
		int c = Integer.parseInt(st.nextToken()); // 초밥 쿠폰
		
		int[] table = new int[N];
		int[] num = new int[d+1];
		
		int cnt = 0;
		int sol = 0;
		
		for (int i=0; i<N; i++) {
			table[i] = Integer.parseInt(br.readLine());
		}
		
		for (int i=N-k; i<N; i++) {
			
			if (num[table[i]]++ == 0) {
				cnt++;
			}
		}
		sol = cnt;
		
		int j = N-k;
		for (int i=0; i<N; i++) {
			
			if (--num[table[j]] == 0) {
				cnt--;
			}
			
			if (num[table[i]]++ == 0) {
				cnt++;
			}
			
			if (num[c] == 0) {
//				System.out.println((j+1)%N + " " + i + " " + (cnt+1));
				sol = Math.max(sol, cnt+1);
			} else {
//				System.out.println((j+1)%N + " " + i + " " + cnt);
				sol = Math.max(sol, cnt);
			}
			
			j = (j+1)%N;
			
			
			
		}
		
		System.out.println(sol);
		
		
		
		

	}

}
