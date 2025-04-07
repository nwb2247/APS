import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int[] score = new int[]{0,1,2,4,8};
		
		int TC = Integer.parseInt(br.readLine());
		
		for (int tc=1; tc<=TC; tc++) {
			
			int K = Integer.parseInt(br.readLine()); // 회전 횟수
			
			int[][] magnets = new int[5][8];
			for (int i=1; i<=4; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j=0; j<8; j++) {
					magnets[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			int[] head = new int[5]; // 빨간 화살표가 가리키는 인덱스 (init : 0, 왼쪽 (head[i]+8-2)%8 오른쪽 (head[i]+8+2)%8)
			
			int sol = 0;
			
			for (int k=0; k<K; k++) {
				st = new StringTokenizer(br.readLine());
				
				int idx = Integer.parseInt(st.nextToken());
				int[] dir = new int[5];
				dir[idx] = Integer.parseInt(st.nextToken());
				
				for (int i=idx; i>=2; i--) {
					int curLeft = (head[i]+8-2)%8;
					int prevRight = (head[i-1]+8+2)%8;
					if (magnets[i][curLeft] == magnets[i-1][prevRight]) break;
					
					dir[i-1] = dir[i]*(-1);

				}
				
				for (int i=idx; i<=3; i++) {
					int curRight = (head[i]+8+2)%8;
					int nextLeft = (head[i+1]+8-2)%8;
					if (magnets[i][curRight] == magnets[i+1][nextLeft]) break;
					dir[i+1] = dir[i]*(-1);
				}
				
				for (int i=1; i<=4; i++) {
					head[i] = (head[i]+(-1)*dir[i]+8)%8;
				}
				
			}
			
			for (int i=1; i<=4; i++) {
				sol += magnets[i][head[i]]*score[i];
			}
			
			
			sb.append("#").append(tc).append(" ").append(sol).append("\n");
			
		}
		
		System.out.println(sb.toString());
 
	}

}
