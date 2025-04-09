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
		int[][] dist = new int[N+1][N+1]; // dist[s][e] : s에서 e로 가는 (최단)거리
		int INF = Integer.MAX_VALUE/2;
		// INF끼리 더하는 경우가 발생하므로 overflow 방지 위해 2로 나눠줌
		for (int i=1; i<=N; i++) {
			Arrays.fill(dist[i], INF);
			dist[i][i] = 0;
		}
		
		for (int i=0; i<M; i++) { // 같은 시작, 도착 지점의 노선이 하나가 아닐 수 있으므로 최소값 갱신 필요
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			int d = Integer.parseInt(st.nextToken());
			if (dist[s][e] < d) continue;
			dist[s][e] = d;
		}
		
		for (int k=1; k<=N; k++) { // 중간에 들릴 지점
			for (int s=1; s<=N; s++) {
				for (int e=1; e<=N; e++) {
					if (dist[s][e] < dist[s][k] + dist[k][e]) continue;
					dist[s][e] = dist[s][k] + dist[k][e];
				}
			}
		}
		
		for (int s=1; s<=N; s++) {
			for (int e=1; e<=N; e++) {
				if (dist[s][e] == INF) {
					sb.append(0).append(" ");
					continue;
				}
				sb.append(dist[s][e]).append(" ");
			}
			sb.append("\n");
		}
		
		System.out.println(sb.toString());
		

	}

}


