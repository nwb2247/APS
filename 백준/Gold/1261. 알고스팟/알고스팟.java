import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int[][] dir = new int[][] {{0,1}, {1,0}, {-1,0}, {0,-1}};
		
		int M = Integer.parseInt(st.nextToken());
		int N = Integer.parseInt(st.nextToken());
		
		int[][] map = new int[N][M];
		
		for (int r=0; r<N; r++) {
			char[] chars = br.readLine().toCharArray();
			for (int c=0; c<M; c++) {
				map[r][c] = chars[c]-'0';
			}
		}
		
		int[][] dist = new int[N][M];
		for (int r=0; r<N; r++) {
			Arrays.fill(dist[r], Integer.MAX_VALUE);
		}
		dist[0][0] = 0;
		
		boolean[][] check = new boolean[N][M];
		
		PriorityQueue<Node> pq = new PriorityQueue<>();
		
		pq.add(new Node(0,0,dist[0][0]));
		
		while (!pq.isEmpty()) {
			
			Node cur = pq.poll();
			if (check[cur.r][cur.c]) continue;
			check[cur.r][cur.c] = true;
			
			if (cur.r == N-1 && cur.c == M-1) break;
			
			for (int d=0; d<4; d++) {
				int nr = cur.r + dir[d][0];
				int nc = cur.c + dir[d][1];
				if (nr<0 || nc<0 || nr>=N || nc>=M) continue;
				int ndist = cur.dist + map[nr][nc];
				if (dist[nr][nc] < ndist) continue;
				dist[nr][nc] = ndist;
				pq.add(new Node(nr, nc, ndist));
			}
			
		}
		
		System.out.println(dist[N-1][M-1]);
				

	}

}

class Node implements Comparable<Node> {
	
	int r, c, dist;

	public Node(int r, int c, int dist) {
		this.r = r;
		this.c = c;
		this.dist = dist;
	}

	@Override
	public int compareTo(Node o) {
		return dist-o.dist;
	}
	
	
	
}
