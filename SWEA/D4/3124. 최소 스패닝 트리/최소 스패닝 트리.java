import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Solution {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		
		for (int t=1; t<=T; t++) {
			st = new StringTokenizer(br.readLine());
			int V = Integer.parseInt(st.nextToken());
			int E = Integer.parseInt(st.nextToken());
			
			boolean[] visited = new boolean[V+1];
			ArrayList<ArrayList<int[]>> adjList = new ArrayList<>();
			for (int i=0; i<=V; i++) {
				adjList.add(new ArrayList<>());
			}
			
			for (int i=0; i<E; i++) {
				st = new StringTokenizer(br.readLine());
				int u = Integer.parseInt(st.nextToken());
				int v = Integer.parseInt(st.nextToken());
				int w = Integer.parseInt(st.nextToken());
				adjList.get(u).add(new int[] {v, w}); 
				adjList.get(v).add(new int[] {u, w});
			}
			
			PriorityQueue<int[]> pq = new PriorityQueue<>(((o1, o2) -> o1[1] - o2[1])); // 최소 힙
			int cnt = 0;
			long sum = 0;
			pq.add(new int[] {1, 0}); // 임의의 정점 하나를 최소 힙에 추가 (가중치는 0)
			
			while (cnt < V) {
				int[] e = pq.poll();
				if (visited[e[0]]) continue;
				/*
				 * 넣을 때 visited 여부를 확인하는데 왜 꺼낼 때도 visited 여부를 확인하는가?
				 *  => 넣을 때는 방문하지 않았지만, 다른 간선에 의해 도달되면서 방문될 수 있기 때문이다.
				 */
				visited[e[0]] = true;
				cnt++;
				sum += e[1];
				for (int[] nextE : adjList.get(e[0])) {
					if (visited[nextE[0]]) continue; // 넣을 때 visited 여부를 확인하면서 불필요한 간선 추가를 방지
					pq.add(nextE);
				}
			}
			
			sb.append("#").append(t).append(" ").append(sum).append("\n");
			
		}
		
		System.out.println(sb.toString());

	}

}
