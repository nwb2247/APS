import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	static int N;
	static boolean[] col, slash, bSlash; // 같은열 대각선(/) 대각선(\)
	static int cnt;

	public static void main(String[] args) throws IOException{
		
		/*
		 * N Queen문제 푸는 방법
		 * 1. 2차원 배열 boolean + drdc을 사용
		 * 2. boolean 1차원배열 3개를 관리한다 (col, slash bSlash). (각 인덱스는 열을 의미) 
		 * 		기존에 같은 행인 퀸이 있다면 not promising
		 * 		같은 열(인덱스)인 퀸이 있어도 not promising
		 * 		대각선은 slash bSlash 로 확인
		 * 
		 * => 위 방법 중 하나를 택하여 백트래킹을 수행한다.
		 * 
		 */
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		col = new boolean[N];
		slash = new boolean[2*N]; 	// (/)방향 대각선은 r+c가 동일 (합의 범위가 0 ~ 2*(N-1)이므로 2*N 배열 생성) 
		bSlash = new boolean[2*N];	// (\)방향 대각선은 r-c가 동일 (차의 범위가 -(N-1) ~ (N-1)이므로 2*N 배열 생성하고 N더해서 관리) 
		
		cnt = 0;
		DFS(0);
		System.out.println(cnt);

	}
	
	private static void DFS(int r) {
		
		if(r>=N) {
			cnt++;
			return;
		}
		
		for (int c=0; c<N; c++) {
			//가지치기
			if(!isAvailable(r, c)) continue;
			col[c] = slash[r+c] = bSlash[r-c+N] = true;
			DFS(r+1); // 다음퀸 놓기
			col[c] = slash[r+c] = bSlash[r-c+N] = false;
		}	
		
	}
	
	private static boolean isAvailable(int r, int c) {
		return !col[c] && !slash[r+c] && !bSlash[r-c+N];
	}

}
