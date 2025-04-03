import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static int V, E;
	static ArrayList<ArrayList<int[]>> adjList;

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		V = Integer.parseInt(st.nextToken());
		E = Integer.parseInt(st.nextToken());
		
		adjList = new ArrayList<>(V+1);
		for (int i=0; i<=V; i++) {
			adjList.add(new ArrayList<>());
		}
		for (int i=0; i<E; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());
			adjList.get(a).add(new int[] {b, w});
			adjList.get(b).add(new int[] {a, w});
		}
		
		st = new StringTokenizer(br.readLine());
		int v1 = Integer.parseInt(st.nextToken());
		int v2 = Integer.parseInt(st.nextToken());
		
		int first_v1 = doDijkstra(1, v1);
		int first_v2 = doDijkstra(1, v2);
		int v1_v2 = doDijkstra(v1, v2); // 무향 그래프 이므로 v1_v2만 확인하면 됨.
		int last_v1 = doDijkstra(V, v1);
		int last_v2 = doDijkstra(V, v2);
		
		int path1 = 0;
		if (first_v1 == Integer.MAX_VALUE ||
			v1_v2 == Integer.MAX_VALUE ||
			last_v2 == Integer.MAX_VALUE) {
			path1 = Integer.MAX_VALUE;
		} else {
			path1 = first_v1 + v1_v2 + last_v2;
		}
		
		int path2 = 0;
		if (first_v2 == Integer.MAX_VALUE ||
			v1_v2 == Integer.MAX_VALUE ||
			last_v1 == Integer.MAX_VALUE) {
			path2 = Integer.MAX_VALUE;
		} else {
			path2 = first_v2 + v1_v2 + last_v1;
		}
		
		int sol = Math.min(path1, path2);
		if (sol == Integer.MAX_VALUE) {
			System.out.println(-1);
		} else {
			System.out.println(sol);
		}
		
		
	}
	
	private static int doDijkstra(int start, int dest) {
		
		int[] dist = new int[V+1];
		Arrays.fill(dist, Integer.MAX_VALUE);
		dist[start] = 0;
		
		boolean[] check = new boolean[V+1];
		
		Queue<int[]> pq = new PriorityQueue<>((o1,o2)->o1[1]-o2[1]);
		pq.add(new int[] {start, dist[start]});
		while(!pq.isEmpty()) {
			int curV = pq.poll()[0];
			if (check[curV]) continue;
			check[curV] = true;
			
			if (curV == dest) break;
			
			for (int[] e : adjList.get(curV)) {
				int nextV = e[0];
				int nextDist = dist[curV] + e[1];
				if (dist[nextV] <= nextDist) continue;
				dist[nextV] = nextDist;
				pq.offer(new int[] {nextV, nextDist});
			}
		}
		
		return dist[dest];
		
	}
}

