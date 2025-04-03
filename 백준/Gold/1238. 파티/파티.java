import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int X = Integer.parseInt(st.nextToken());
		
		ArrayList<ArrayList<int[]>> adjList1 = new ArrayList<>(N+1);
		ArrayList<ArrayList<int[]>> adjList2 = new ArrayList<>(N+1);
		for (int i=0; i<=N; i++) {
			adjList1.add(new ArrayList<>());
			adjList2.add(new ArrayList<>());
		}
		
		for (int i=0; i<M; i++) {
			st  = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());
			adjList1.get(start).add(new int[] {end, w}); // X에서 각 집으로 돌아갈 때 최단 거리
			adjList2.get(end).add(new int[] {start, w}); // 각 집에서 X로 갈때 최단 거리 
			// adjList1을 뒤집음으로써 각집->X 이 X->각집으로 뒤집힘. 따라서 X에서 모든 정점의 최단 거리 구하여 각집에서 X로 갈 때 최단 거리 구할 수 있음
		}
		
		int[] dist1 = new int[N+1];
		int[] dist2 = new int[N+1];
		Arrays.fill(dist1, Integer.MAX_VALUE);
		Arrays.fill(dist2, Integer.MAX_VALUE);
		dist1[X] = 0;
		dist2[X] = 0;
		
		boolean[] check1 = new boolean[N+1];
		boolean[] check2 = new boolean[N+1];
		
		doDijkstra(X, adjList1, dist1, check1);
		doDijkstra(X, adjList2, dist2, check2);
		
		int max = 0;
		for (int i=0; i<=N; i++) {
			max = Math.max(max, dist1[i]+dist2[i]);
		}
		
		System.out.println(max);
		
	}
	
	private static void doDijkstra(int start, ArrayList<ArrayList<int[]>> adjList, int[] dist, boolean[] check) {
		
		Queue<int[]> pq = new PriorityQueue<>((o1,o2) -> o1[1]-o2[1]);
		pq.offer(new int[] {start, dist[start]});
		while (!pq.isEmpty()) {
			
			int curV = pq.poll()[0];
			if (check[curV]) continue;
			check[curV] = true;
			
			for (int[] e : adjList.get(curV)) {
				int nextV = e[0];
				int nextDist = dist[curV] + e[1];
				if (dist[nextV] <= nextDist) continue;
				dist[nextV] = nextDist;
				pq.offer(new int[] {nextV, nextDist});
			}
			
 		}
		
	}

}