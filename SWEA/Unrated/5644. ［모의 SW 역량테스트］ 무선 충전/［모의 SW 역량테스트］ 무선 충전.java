import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	
	static int[] dr = {0,0,1,0,-1};
	static int[] dc = {0,-1,0,1,0};
	// 지도 밖으로 나가는 입력은 존재 x

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		
		for (int t=1; t<=T; t++) {
			st = new StringTokenizer(br.readLine());
			int M = Integer.parseInt(st.nextToken());	// 이동 시간
			int N = Integer.parseInt(st.nextToken());	// BC 갯수
			
			
			// 1. 이동 경로 저장
			// 0초부터 충전하므로 배열 길이 M+1
			// A[i] 충전완료하고 이동방향 => i+1초에 반영
			int[] A = new int[M+1];
			st = new StringTokenizer(br.readLine());
			for (int i=0; i<M; i++) {
				A[i] = Integer.parseInt(st.nextToken());
			}
			
			int[] B = new int[M+1];
			st = new StringTokenizer(br.readLine());
			for (int i=0; i<M; i++) {
				B[i] = Integer.parseInt(st.nextToken());
			}
			
			
			// 2. BC 범위 저장
			int[] BC = new int[N];
			boolean[][][] map = new boolean[10+1][10+1][N];
			
			for (int i=0; i<N; i++) {
				st = new StringTokenizer(br.readLine());
				int centerR = Integer.parseInt(st.nextToken());
				int centerC = Integer.parseInt(st.nextToken());
				int C = Integer.parseInt(st.nextToken());
				BC[i] = Integer.parseInt(st.nextToken());
				
				// 사각형 범위를 지정하고 그 안에서 맨해튼 거리 조건을 만족하는 범위를 true로 지정
				int minR = Math.max(1, centerR-C);
				int maxR = Math.min(10, centerR+C);
				int minC = Math.max(1, centerC-C);
				int maxC = Math.min(10, centerC+C);
				
				for (int r=minR; r<=maxR; r++) {
					for (int c=minC; c<=maxC; c++) {
						if (Math.abs(r-centerR)+Math.abs(c-centerC) > C) continue;
						map[r][c][i] = true;
					}
				}
				
			}
			
			// 3. 이동 경로 반영하며 충전 최대값 더하기
			int Ar = 1;
			int Ac = 1;
			int Br = 10;
			int Bc = 10;
			
			int cnt = 0;
			
			for (int i=0; i<=M; i++) {
				
				// 각 칸에서의 최대 충전 값
				int max = 0;
				
				for (int j=0; j<N; j++) {
					// 둘 중 하나만 충전하는 경우 또는 같은 BC로 충전하는 경우 
					if (map[Ar][Ac][j] || map[Br][Bc][j]) {
						max = Math.max(max, BC[j]);
					}
					
					// 둘 다 충전하되, 서로 다른 BC로 충전하는 경우
					for (int k=0; k<N; k++) {
						if (map[Ar][Ac][j] && map[Br][Bc][k] && j!=k) {
							max = Math.max(max, BC[j] + BC[k]);						
						}
					}
				}
				
//				System.out.println(i + " Ar" + Ar + " Ac" + Ac + " Br" +Br+ " Bc" + Bc + " " + max);
				
				cnt += max;
				
				// 다음 좌표로 업데이트
				Ar += dr[A[i]];
				Ac += dc[A[i]];
				Br += dr[B[i]];
				Bc += dc[B[i]];
				
			}
			
			sb.append("#").append(t).append(" ").append(cnt).append("\n");
		}
		
		System.out.println(sb);
		
	}

}
