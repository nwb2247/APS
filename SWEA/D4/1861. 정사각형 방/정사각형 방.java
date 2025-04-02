import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {
	
	static int N;
	static int[][] map;
	static boolean[][] visited;
	
	static int[] dr = {0,0,1,-1};
	static int[] dc = {1,-1,0,0};

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		
		for (int t=1; t<=T; t++) {
			
			// 입력
			N = Integer.parseInt(br.readLine());
			map = new int[N][N];
			
			for (int r=0; r<N; r++) {
				st = new StringTokenizer(br.readLine());
				for (int c=0; c<N; c++) {
					map[r][c] = Integer.parseInt(st.nextToken());
				}
			}
			
			// 풀이
			int maxCnt = 0;
			int minIdx = Integer.MAX_VALUE;
			visited = new boolean[N][N];
			
			// 각 좌표를 돌면서 BFS를 통해 연결된(1만큼 차이나는) 모든 좌표를 찾고, 그 중 가장 작은 인덱스를 갱신한다.
			// 연결이 끊기면 다음 좌표부터 다시 BFS를 돌리되, 이미 방문한 좌표는 다른 연결 그래프의 일부이므로 패스한다.
			for (int r=0; r<N; r++) {
				for (int c=0; c<N; c++) {
					
					// 연결이 끊기면 다음 좌표부터 다시 BFS를 돌리되, 이미 방문한 좌표는 다른 연결 그래프의 일부이므로 패스한다.
					if (visited[r][c]) continue;
					
					// BFS 수행 
					int[] minIdx_maxCnt = BFS(r,c);
					
					// 최대 연결 그래프 or (같은 크기의 그래프면) 최소 인덱스 갱신
					if (minIdx_maxCnt[1] == maxCnt) {
						minIdx = Math.min(minIdx, minIdx_maxCnt[0]);
					} else if (minIdx_maxCnt[1] > maxCnt) {
						maxCnt = minIdx_maxCnt[1];
						minIdx = minIdx_maxCnt[0];
					}
				}
			}
			
			sb.append("#"+t+" "+minIdx+" "+maxCnt+"\n");
			
		}
		
		System.out.println(sb);

	}
	
	// 이미 지나온 방을 다시 지나갈 수 없다는 제약이 존재하지 않음
	// 따라서 시작지점은 연결된 모든 방 중 가장 작은 번호로 설정하면 됨
	private static int[] BFS(int inputR, int inputC) {
		
		int[] minIdx_maxCnt = new int[2];
		minIdx_maxCnt[0] = Integer.MAX_VALUE;
		
		Queue<int[]> queue = new ArrayDeque<>();
		queue.add(new int[] {inputR,inputC});
		
		while (!queue.isEmpty()) {
			
			int[] coord = queue.poll();
			int r=coord[0];
			int c=coord[1];
			
			for (int d=0; d<4; d++) {
				int nr = r+dr[d];
				int nc = c+dc[d];
				
				// 유효하지 않은 좌표 패스, 이미 방문한 좌표 패스
				if (nr >= N || nc >= N || nr < 0 || nc < 0 || visited[nr][nc]) continue;
				
				// 이미 방문한 좌표는 패스
				int diff = map[nr][nc] - map[r][c];
				
				// 1만큼만 차이 나면 큐에 삽입
				if (diff == 1 || diff == -1) {
					queue.add(new int[] {nr,nc});
					visited[nr][nc] = true;
					minIdx_maxCnt[1]++;
					minIdx_maxCnt[0] = Math.min(minIdx_maxCnt[0], map[nr][nc]);
				}			
			}
			
		}
		return minIdx_maxCnt;
		
	}

}
