import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		// 플로이드 워셜 응용 (모든 정점에서 모든 정점으로 가는 방법이 있는가?)
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int TC = Integer.parseInt(br.readLine());
		for (int tc=1; tc<=TC; tc++) {
			
			int N = Integer.parseInt(br.readLine());
			
			int[][] coord = new int[N+2][2]; // 0:집 1~N:편의점 N+1:도착지
			for (int i=0; i<N+2; i++) {
				st = new StringTokenizer(br.readLine());
				coord[i][0] = Integer.parseInt(st.nextToken());
				coord[i][1] = Integer.parseInt(st.nextToken());
			}
			
			boolean[][] possible = new boolean[N+2][N+2];
			for (int s=0; s<N+2; s++) {
				for (int e=0; e<N+2; e++) {
					// 맨해튼 거리 계산후 1000보다 가까우면 도달가능
					int d = Math.abs(coord[s][0]-coord[e][0])+Math.abs(coord[s][1]-coord[e][1]);
					if (d <= 1000) possible[s][e] = true;
				}
			}
			
			// 플로이드 워셜을 통해 각 편의점을 추가로 들리면 도달가능해지는지 확인
			for (int k=0; k<N+2; k++) {
				for (int s=0; s<N+2; s++) {
					for (int e=0; e<N+2; e++) {
						if (possible[s][e]) continue;
						if (possible[s][k] && possible[k][e]) possible[s][e] = true;
					}
				}
			}
			
			// 집부터 축제까지 도달가능 여부확인
			if (possible[0][N+1]) {
				sb.append("happy");
			} else {
				sb.append("sad");
			}
			sb.append("\n");			
			
		}
		
		System.out.println(sb.toString()); 
		

	}

}
