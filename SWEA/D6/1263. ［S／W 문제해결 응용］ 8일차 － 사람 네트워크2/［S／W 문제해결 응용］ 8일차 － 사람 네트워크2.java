import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int TC = Integer.parseInt(br.readLine());
		
		for (int tc=1; tc<=TC; tc++) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int[][] dist = new int[N][N]; // dist[s][e] s에서 e로 가는 거리
			for (int s=0; s<N; s++) {
				for (int e=0; e<N; e++) {
					dist[s][e] = Integer.parseInt(st.nextToken());
					if (dist[s][e] != 0) continue;
					dist[s][e] = Integer.MAX_VALUE/2;
					// INF끼리 더하는 경우가 있으므로 overflow 방지 위해 2로 나눠줌
				}
				dist[s][s] = 0;
			}
			
			for (int k=0; k<N; k++) {
				for (int s=0; s<N; s++) {
					for (int e=0; e<N; e++) {
						if (dist[s][e] < dist[s][k]+dist[k][e]) continue;
						dist[s][e] = dist[s][k]+dist[k][e];
					}
				}
			}
			
			int sol = Integer.MAX_VALUE;
			for (int s=0; s<N; s++) {
				int sum = 0;
				for (int e=0; e<N; e++) {
					sum += dist[s][e];
				}
				if (sol < sum) continue;
				sol = sum;
			}
			
			sb.append("#").append(tc).append(" ").append(sol).append("\n");
			
		}
		
		System.out.println(sb.toString());
		

	}

}

