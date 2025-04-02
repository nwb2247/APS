import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	/*
	 * BFS : "너비" 우선 탐색이므로 최단 경로 탐색 가능 (단, 가중치가 다 다른경우는 적용이 어려움) 
	 * 최단 경로를 탐색할 때, 큐에 넣는 순서가 매우 중요함
	 * 
	 * 큐에 넣어서 dest 정점이 나올 때 바로 리턴하는 방식이므로
	 * dest 정점까지 하는 경로가 여러개일때, 순서를 고려하지 않으면 원하는 경로가 나오지 않을 수 있음
	 * (단 가중치가 동일하고 거리만 계산하는 경우, 어떤 경로를 선택해도 무관하므로 상관 x)
	 * 
	 * 아래의 경우에는 2배가 되는 하위노드에 대해서 거리가 동일하므로 가장 먼저 넣어, 나중에 가장 먼저 poll 되도록 해야함
	 * -1의 경우에도 마찬가지로 -1 하고 *2 했을때가 최단 경로인 경우가 있으므로 +1 노드 보다 먼저 넣어줘야함
	 * 
	 * 
	 */
	
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		int M = Math.max(N, K);
		
		int[][] graph = new int[2*M+1][3];		
		
		for (int i=0; i<=2*M; i++) {
			
			graph[i][0] = (2*i>2*M)? -1 : 2*i; // *2
			graph[i][1] = (i-1<0)? -1 : i-1; // -1
			graph[i][2] = (i+1>2*M)? -1 : i+1; // 1	
			
		}

		boolean[] visited = new boolean[2*M+1];
		int[] distToN = new int[2*M+1];
		
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
				if (i == 0) {
					distToN[next] = distToN[node];
				} else {
					distToN[next] = distToN[node]+1;
				}
				
			}
			
		}
	

	}

}
