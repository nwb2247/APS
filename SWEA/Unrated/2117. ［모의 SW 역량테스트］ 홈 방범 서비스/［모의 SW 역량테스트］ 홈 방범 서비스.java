import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solution {
	
	static int N, M;
	static ArrayList<int[]> hList;
	static int[] cost;
	
	static {
		cost = new int[20+2]; // 20의 경우 짝수이므로 K=21까지 확인해야함
		for (int k=1; k<20+2; k++) {
			cost[k] = k*k+(k-1)*(k-1);
		}
	}
	
	static int sol = 0;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		
		int T = Integer.parseInt(br.readLine());
		for (int t=1; t<=T; t++) {
			
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			
			hList = new ArrayList<>();
			
			for (int r=0; r<N; r++) {
				st = new StringTokenizer(br.readLine());
				for (int c=0; c<N; c++) {
					int val = Integer.parseInt(st.nextToken());
					if (val == 0) continue;
					hList.add(new int[] {r,c});
				}
			}
			
			sol = 0;
			
			for (int r=0; r<N; r++) {
				for (int c=0; c<N; c++) {
					for (int k=1; k<=N+1; k++) { // k가 짝수인 경우 고려해서 N+1까지 확인
						int cnt = 0;
						for (int[] h : hList) {
							if (Math.abs(r-h[0]) + Math.abs(c-h[1]) <= k-1) cnt++;
						}
						if (cnt*M < cost[k]) continue;
						sol = Math.max(sol, cnt);
					}
				}
			}
			
			sb.append("#").append(t).append(" ").append(sol).append("\n");
			
			
		}
		
		System.out.println(sb.toString());
		
		
		

	}

}
