import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	
	// BJ1244
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		
		int[] switches = new int[N+1];
		for (int i=1; i<=N; i++) {
			switches[i] = Integer.parseInt(st.nextToken());
		}
		
		int M = Integer.parseInt(br.readLine());
		
		for (int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int num = Integer.parseInt(st.nextToken());
			
			if (s == 1) {
				for (int j=num; j<=N; j += num) {
					if (switches[j] == 1) {
						switches[j] = 0;
					} else {
						switches[j] = 1;
					}
				}
			} else { // s==2
				for (int j=0; num+j<=N && num-j>=1; j++) {
					if (switches[num+j] != switches[num-j]) {
						break;
					}
					if (switches[num+j] == 1) {
						switches[num+j] = 0;
						switches[num-j] = 0;
					} else {
						switches[num+j] = 1;
						switches[num-j] = 1;
					}
					
				}
			}
		}
		
		StringBuilder sb = new StringBuilder();
		
		for (int i=1; i<=N; i++) {
			sb.append(switches[i] + " ");
			if (sb.length() == 40) {
				System.out.println(sb);
				sb = new StringBuilder();
			}
		}
		
		System.out.println(sb);
	

	}

}
