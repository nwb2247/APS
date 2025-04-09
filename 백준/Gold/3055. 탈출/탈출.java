import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int R = Integer.parseInt(st.nextToken());
		int C = Integer.parseInt(st.nextToken());
		
		// 물과 비버 모두 pq로 관리
		Queue<int[]> pqS = new ArrayDeque<>();
		Queue<int[]> pqW = new ArrayDeque<>();
				
		int[][] dir = {{0,1},{0,-1},{1,0},{-1,0}};
		
		
		// 물은 비어있거나 S인 경우 pq에 추가
		
		char[][] map = new char[R][];
		for (int r=0; r<R; r++) {
			map[r] = br.readLine().toCharArray();
			for (int c=0; c<C; c++) {
				switch(map[r][c]) {
				case '*' : 
					pqW.add(new int[] {r, c, 0});
					break;
				case 'S' : 
					pqS.add(new int[] {r, c, 0});
					break;
				}
			}
		}
		
		
		int t = 0;
		outer : 
		while (true) {
			
			while (!pqW.isEmpty() && pqW.peek()[2] == t) {
				int[] w = pqW.poll();
				int r = w[0];
				int c = w[1];
				
				for (int d=0; d<4; d++) {
					int nr = r+dir[d][0];
					int nc = c+dir[d][1];
					if (nr>=R || nc>=C || nr<0 || nc<0) continue;
					if (map[nr][nc] == 'S' || map[nr][nc] == '.') {
						pqW.add(new int[] {nr, nc, t+1});
						map[nr][nc] = '*';
					}
				}
			}
			
//			for (int i=0; i<R; i++) {
//				System.out.println(Arrays.toString(map[i]));
//			}
			
			if (pqS.isEmpty()) {
				System.out.println("KAKTUS");
				break outer;
			}
			
			while (!pqS.isEmpty() && pqS.peek()[2] == t) {
				int[] s = pqS.poll();
				int r = s[0];
				int c = s[1];
				
				for (int d=0; d<4; d++) {
					int nr = r+dir[d][0];
					int nc = c+dir[d][1];
					if (nr>=R || nc>=C || nr<0 || nc<0) continue;
					if (map[nr][nc] == 'D') {
						System.out.println(t+1);
						break outer;
					}
					if (map[nr][nc] == '.') {
						pqS.add(new int[] {nr, nc, t+1});
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


