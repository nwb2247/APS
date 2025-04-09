import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		
		int TC = sc.nextInt();
		
		for (int tc=1; tc<=TC; tc++) {
			int N = sc.nextInt();
			int[][] dist = new int[N][N]; // dist[s][e] s에서 e로 가는 거리
			for (int s=0; s<N; s++) {
				for (int e=0; e<N; e++) {
					dist[s][e] = sc.nextInt();
					if (dist[s][e] != 0) continue;
					dist[s][e] = Integer.MAX_VALUE/2;
					// INF끼리 더하는 경우가 있으므로 overflow 방지 위해 2로 나눠줌
				}
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
			sol = sol-2;
			
			sb.append("#").append(tc).append(" ").append(sol).append("\n");
			
		}
		
		System.out.println(sb.toString());
		

	}

}

