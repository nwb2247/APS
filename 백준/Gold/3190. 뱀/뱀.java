import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		int K=  Integer.parseInt(br.readLine());
		
		int[][] dir = new int[][] {{0,1},{1,0},{0,-1},{-1,0}};
		
		int[][] map = new int[N+2][N+2];
		
		for (int i=0; i<K; i++) {
			st = new StringTokenizer(br.readLine());
			map[Integer.parseInt(st.nextToken())][Integer.parseInt(st.nextToken())] = 2;
		}
		map[1][1] = 1;
		
		ArrayDeque<int[]> pos = new ArrayDeque<>();
		pos.add(new int[] {1,1});
		int d = 0;
		int sec = 0;
		
		int L = Integer.parseInt(br.readLine());
		
		ArrayDeque<int[]> op = new ArrayDeque<>();
		
		for (int i=0; i<L; i++) {
			st = new StringTokenizer(br.readLine());
			int opSec = Integer.parseInt(st.nextToken());
			String opDir = st.nextToken();
			
			if (opDir.equals("L")) {
				op.offerLast(new int[] {opSec, -1});
			} else {
				op.offerLast(new int[] {opSec, 1});
			}
		}
		
		while (true) {
			if (!op.isEmpty() && sec == op.peekFirst()[0]) {
				d = (d+4+op.pollFirst()[1])%4;
			}
			
			
			int newX = pos.peekFirst()[0] + dir[d][0];
			int newY = pos.peekFirst()[1] + dir[d][1];
			
			if (newX > N || newY > N || newX < 1 || newY < 1
					|| map[newX][newY] == 1) {
				break;
			} else {
				pos.addFirst(new int[] {newX, newY});
				if (map[newX][newY] != 2) {
					int[] tail = pos.pollLast();
					map[tail[0]][tail[1]] = 0;
				}
				map[newX][newY] = 1;				
			}
			
			sec++;
			
//			System.out.println(sec);
//			for (int i=0; i<=N+1; i++) {
//				System.out.println(Arrays.toString(map[i]));
//			}
		
		}
		
		System.out.println(sec+1);
		
		
		
		
		
		
	}
}