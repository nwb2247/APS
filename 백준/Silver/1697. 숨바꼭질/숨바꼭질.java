import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	// BFS : "너비" 우선 탐색이므로 최단 경로(가중
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		int M = Math.max(N, K); // M : N과 K중 최대값
		
		int[][] graph = new int[2*M+1][3];		
		
		for (int i=0; i<=2*M; i++) {
			
			graph[i][0] = (i-1<0)? -1 : i-1;
			graph[i][1] = (i+1>2*M)? -1 : i+1;
			graph[i][2] = (2*i>2*M)? -1 : 2*i;
			
		}


		boolean[] visited = new boolean[2*M+1];
		int[] distToN = new int[2*M+1]; // 배열을 통해 BFS를 통한 N까지의 최단거리 기록 
		
		Queue<Integer> q = new ArrayDeque<>();
		
		
		
		// 시작 노드 삽입
		q.add(N);
		visited[N] = true;
		
		
		while(!q.isEmpty()) {
			
			int node = q.poll();
			
			if (node == K) {
				System.out.println(distToN[node]);
				break;
			}
					
			for (int i=0; i<3; i++) {
				int next = graph[node][i];
				if (next == -1 || visited[next]) { // 하위 노드가 없거나 방문한 노드라면 패스
					continue;
				}
				
				q.add(next);
				visited[next] = true;
				distToN[next] = distToN[node]+1; // 새로운 하위 노드 탐색시 거리를 1추가
				
			}
			
		}
	

	}

}
