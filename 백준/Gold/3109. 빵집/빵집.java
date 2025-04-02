import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int R, C;
	static boolean[][] visitedDown;
	static boolean[][] visitedUp;
	static int[] nextR;
	
	static int downCnt, upCnt;

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		
		visitedDown = new boolean[R][C];
		visitedUp = new boolean[R][C];
		nextR = new int[C];
		
		for (int r=0; r<R; r++) {
			char[] chars = br.readLine().toCharArray();
			for (int c=0; c<C; c++) {
				if (chars[c] == '.') continue;
				visitedDown[r][c] = visitedUp[r][c] = true; //'x'
			}
		}
		
//		System.out.println(Arrays.deepToString(visitedDown));
		
		// 파이프라인 간에 크로스나 겹치기 되지 않으므로 그리디로 계산 (맨 위, 맨 아래부터 계산하고 갱신)
		for (int r=0; r<R; r++) {
			downDFS(r,0);
		}
		
//		for (int r=R-1; r>=0; r--) {
//			upDFS(r,0);
//		}
		
//		System.out.println(downCnt + " " + upCnt);
		
		System.out.println(Math.max(downCnt, upCnt));
		

	}
	
	private static boolean downDFS(int r, int c) {
		
//		System.out.println(r+" "+c);
		if (c == C-1) {
			downCnt++;
			return true;
		}
		
		for (int nextR=r-1; nextR<=r+1; nextR++) {
			if (nextR<0 || nextR>=R || visitedDown[nextR][c+1]) continue;
			visitedDown[nextR][c+1] = true;
			if (downDFS(nextR, c+1)) return true;
		}
		
		return false;
		
	}
	
	private static boolean upDFS(int r, int c) {
		
//		System.out.println(r+" "+c);
		if (c == C-1) {
			upCnt++;
			return true;
		}
		
		for (int nextR=r+1; nextR>=r-1; nextR--) {
			if (nextR<0 || nextR>=R || visitedUp[nextR][c+1]) continue;
			visitedUp[nextR][c+1] = true;
			if (upDFS(nextR, c+1)) return true;
		}
		
		return false;
		
	}

}
