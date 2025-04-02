import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
	
	static int offset = 12;
	static int[] cost = new int[4];
	static int[] period = {1,1,3,12};
	static int[] plan = new int[offset+12];
	static int[][] DP = new int[offset+12][4]; // 최대 정기권 기간이 12달이므로 offset : 12

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		
		for (int t=1; t<=T; t++) {
			
			// init
			st = new StringTokenizer(br.readLine());
			for (int i=0; i<4; i++) {
				// 0:하루비용 1:한달비용 2:세달비용 3:일년비용
				cost[i] = Integer.parseInt(st.nextToken());
			}
			st= new StringTokenizer(br.readLine());
			for (int i=offset; i<offset+12; i++) {
				plan[i] = Integer.parseInt(st.nextToken());
			}
			
			// solve		
			for(int m=offset; m<offset+12; m++) {
				
				int[] min = new int[4]; // min[i] : period[i]달 전 누적합들의 최소
				
				for (int p=0; p<4; p++) {
					min[p] = DP[m-period[p]][0];
					for (int c=1; c<4; c++) {
						min[p] = Math.min(min[p], DP[m-period[p]][c]);
					}
				}
				
				for (int i=1; i<4; i++) {
					DP[m][i] = min[i] + cost[i];
				}
				DP[m][0] = min[0] + cost[0]*plan[m];
				
			}	
			
			int sol = DP[offset+12-1][0];
			for (int i=1; i<4; i++) {
				sol = Math.min(sol, DP[offset+12-1][i]);
			}
			
			sb.append("#"+t+" "+sol+"\n");
			
		}
		
		System.out.println(sb);

	}
	

}
