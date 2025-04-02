import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		int[][] cumSum = new int[N+1][N+1];
		
		for (int r=1; r<=N; r++) {
			st = new StringTokenizer(br.readLine());
			for (int c=1; c<=N; c++) {
				cumSum[r][c] = cumSum[r-1][c] + cumSum[r][c-1] - cumSum[r-1][c-1] 
								+ Integer.parseInt(st.nextToken());
			}
			
		}
		
		StringBuilder sb = new StringBuilder();
		
		for (int m=0; m<M; m++) {
			st = new StringTokenizer(br.readLine());
			int x1 = Integer.parseInt(st.nextToken());
			int y1 = Integer.parseInt(st.nextToken());
			int x2 = Integer.parseInt(st.nextToken());
			int y2 = Integer.parseInt(st.nextToken());
			sb.append(cumSum[x2][y2] - cumSum[x1-1][y2] - cumSum[x2][y1-1] + cumSum[x1-1][y1-1] + "\n");			
		}
		
		System.out.println(sb);


	}

}
