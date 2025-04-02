import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int T = 10;
		
		for(int t=1; t<=T; t++) {
			
			int tnum = Integer.parseInt(br.readLine());
			
			int N = 100;
			int[][] map = new int[N][N];
			
			for(int r=0; r<N; r++) {
				st = new StringTokenizer(br.readLine());
				for (int c=0; c<N; c++) {
					map[r][c] = Integer.parseInt(st.nextToken());
				}
			}
			
			// 맨 마지막 행이 2인 열 찾음
			int endC=0;
			for (; endC<N; endC++) {
				if (map[N-1][endC] == 2) {
					break;
				}
			}
			
			// 도착지점부터 올라가서 시작시점 찾기
			int c=endC; // 현재 위치 도착지점으로 초기화
			int r=N-1;
			int[] dr = {-1,0,0};
			int[] dc = {0,-1,1}; // 0 : 위, 1: 왼쪽; 2: 오른쪽;
			int d = 0;
			
			while(r>0) {
				
				if (d == 0) { // 위로 직진중이었다면
					for (int nd=1; nd<=2; nd++) { // 왼쪽 오른쪽이 1인지 확인
						int nc = c+dc[nd];
						if (nc<N && nc>=0 && map[r][nc] == 1) {
							d = nd;
							break;
						}
					}
					r += dr[d];	// 현재 위치 업데이트
					c += dc[d];
				} else { // 양옆으로 직진중이었다면
					int nr = r+dr[0];	
					if (nr<N && nr>=0 && map[nr][c] == 1) { // 위가 1인지 확인
						d = 0;
					}
					r += dr[d]; // 현재 위치 업데이트
					c += dc[d];
				}
			}
			
			System.out.println("#"+tnum+" "+c);

			
		}


	}

}
