import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int R = Integer.parseInt(st.nextToken());
		int C = Integer.parseInt(st.nextToken());
		
		// 물과 고슴도치 모두 큐로 관리
		Queue<int[]> qS = new ArrayDeque<>();
		Queue<int[]> qW = new ArrayDeque<>();
				
		int[][] dir = {{0,1},{0,-1},{1,0},{-1,0}};
		
		char[][] map = new char[R][];
		for (int r=0; r<R; r++) {
			map[r] = br.readLine().toCharArray();
			for (int c=0; c<C; c++) {
				switch(map[r][c]) {
				case '*' : 
					qW.add(new int[] {r, c, 0});
					break;
				case 'S' : 
					qS.add(new int[] {r, c, 0});
					break;
				}
			}
		}
		
		int t = 0;
		outer : 
		while (true) {
			
			// 물 채움
			// 1초 뒤 물이 차는 곳에 고슴도치가 올 수 없으므로 물부터 채움
			while (!qW.isEmpty() && qW.peek()[2] == t) {
				int[] w = qW.poll();
				int r = w[0];
				int c = w[1];
				for (int d=0; d<4; d++) {
					int nr = r+dir[d][0];
					int nc = c+dir[d][1];
					if (nr>=R || nc>=C || nr<0 || nc<0) continue;
					if (map[nr][nc] == 'S' || map[nr][nc] == '.') { // 고슴도치가 지나간 자리이거나 빈 공간이면 채움
						qW.add(new int[] {nr, nc, t+1});
						map[nr][nc] = '*';
					}
				}
			}
			
//			for (int i=0; i<R; i++) {
//				System.out.println(Arrays.toString(map[i]));
//			}
			
			if (qS.isEmpty()) {	// 고슴도치가 있을 자리가 더이상 없으면 실패
				System.out.println("KAKTUS");
				break outer;
			}
			
			// 고슴도치가 있을 수 있는 자리를 꺼내 1초뒤에 고슴도치가 있을 자리를 채움
			while (!qS.isEmpty() && qS.peek()[2] == t) {
				int[] s = qS.poll();
				int r = s[0];
				int c = s[1];
				
				for (int d=0; d<4; d++) {
					int nr = r+dir[d][0];
					int nc = c+dir[d][1];
					if (nr>=R || nc>=C || nr<0 || nc<0) continue;
					if (map[nr][nc] == 'D') {			// 1초 뒤 비버굴에 도착한다면 리턴
						System.out.println(t+1);
						break outer;
					}
					if (map[nr][nc] == '.') {
						qS.add(new int[] {nr, nc, t+1});
						map[nr][nc] = 'S';
					}
				}
			}
			
//			for (int i=0; i<R; i++) {
//				System.out.println(Arrays.toString(map[i]));
//			}
//			System.out.println();
			
			t++;
			
		}


	}

}


