import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
	
	static int D, W, K;
	static boolean[][] map;
	
	static boolean[][] origin; 	// 원복을 위한 배열
	static boolean[] trueArr;	// true 배열
	static boolean[] falseArr;	// false 배열
	
	static int min;

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		
		for (int t=1; t<=T; t++) {
			
			// 입력 받기
			st = new StringTokenizer(br.readLine());
			
			D = Integer.parseInt(st.nextToken());
			W = Integer.parseInt(st.nextToken());
			K = Integer.parseInt(st.nextToken());
			map = new boolean[D][W];
			
			origin = new boolean[D][W];
			trueArr = new boolean[W];
			falseArr = new boolean[W];
			for (int i=0; i<W; i++) {
				trueArr[i] = true;
			}
			
			min = D;			
			for (int r=0; r<D; r++) {
				st = new StringTokenizer(br.readLine());
				for (int c=0; c<W; c++) {
					int i = Integer.parseInt(st.nextToken());
					if (i==0) continue;
					origin[r][c] = true;
					map[r][c] = true;
				}
			}
			
			
			// DFS 수행 (각 행에 대해)
			for (int r=0; r<D; r++) {
				DFS(r,0);
			}
			
			sb.append("#"+t+" "+min+"\n");	
			
		}
		
		System.out.println(sb);

	}
	
	private static void DFS(int r, int cnt) {
		
		if (cnt >= min) {				// min(지금까지의 최소 투약 수)보다 크거나 같으면 더 이상 진행할 필요 없음
			return;
		}
		
		if (isPass()) {					// 조건을 충족하는지 확인하고 충족한다면 min 값 갱신
			min = Math.min(min, cnt);
			return;
		}
		
		if (r == D) { 					// 끝까지 탐색해 더이상 탐색할 수 없으면 return
			return;
		}
		
		for (int i=r; i<D; i++) {
			map[r] = trueArr;			// true배열로 바꾸고 수행
			DFS(i+1, cnt+1);	
			map[r] = falseArr;			// false배열로 바꾸고 수행
			DFS(i+1, cnt+1);
			map[r] = origin[r];			// 원상복구
		}		
		
	}
	
	private static boolean isPass() { 		// 조건을 충족하는지 확인하는 코드
		
		outer :
		for (int c=0; c<W; c++) {
			int seq = 0;					// 현재 연속된 갯수
			boolean bool = false;
			for (int r=0; r<D; r++) {	
				if (bool != map[r][c]) {	// 새로운 bool이 지금까지의 bool과 다르다면
					bool = !bool;			
					seq = 1;				// seq 초기화
					continue;
				}
				if (++seq >= K) {			// seq이 K넘기면 (즉 조건 충족하면) 다음 열 확인
					continue outer;
				}
			}
			return false;
		}
		
		return true;
	}
	

}


















