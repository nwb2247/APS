import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
		
		int[][] dist = new int[N+1][N+1];
		for (int s=1; s<=N; s++) {
			Arrays.fill(dist[s], Integer.MAX_VALUE/2);
			dist[s][s] = 0;
		}
		int[][] next = new int[N+1][N+1];
		
		for (int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			int d = Integer.parseInt(st.nextToken());
			dist[s][e] = Math.min(dist[s][e], d);
			next[s][e] = e;
		}
		
		for (int k=1; k<=N; k++) {
			for (int s=1; s<=N; s++) {
				for (int e=1; e<=N; e++) {
					if (dist[s][e] <= dist[s][k]+dist[k][e]) continue;
					dist[s][e] = dist[s][k]+dist[k][e];
					next[s][e] = next[s][k];
				}
			}
		}
		
		for (int s=1; s<=N; s++) {
			for (int e=1; e<=N; e++) {
				if (dist[s][e] == Integer.MAX_VALUE/2) {
					sb.append(0);
				} else {
					sb.append(dist[s][e]);
				}
				sb.append(" ");
			}
			sb.append("\n");
		}
		
		for (int s=1; s<=N; s++) {
			for (int e=1; e<=N; e++) {
				if (next[s][e] == 0) {
					sb.append(0).append("\n");
				} else {
					StringBuilder path = new StringBuilder(); // 경로 기록을 위한 StringBuilder
					int cnt = 0;
					int cur = s;
					while (cur != 0) {
						path.append(cur).append(" ");
						cur = next[cur][e];
						cnt++;
					}
					path.insert(0, " ").insert(0, cnt);
					sb.append(path).append("\n");
				}
			}
		}
		
		System.out.println(sb.toString());
//		System.out.println(Arrays.deepToString(next));
		
	}

}

