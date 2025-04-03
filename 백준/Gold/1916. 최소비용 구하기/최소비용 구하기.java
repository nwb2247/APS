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
		StringTokenizer st;
		
		int V = Integer.parseInt(br.readLine());
		int E = Integer.parseInt(br.readLine());
		
		ArrayList<ArrayList<int[]>> adjList = new ArrayList<>(V+1);
		for (int i=0; i<=V; i++) {
			adjList.add(new ArrayList<>());
		}
		
		for (int i=0; i<E; i++) {
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());
			adjList.get(start).add(new int[] {end, w});
		}
		
		st = new StringTokenizer(br.readLine());
		int start = Integer.parseInt(st.nextToken());
		int dest = Integer.parseInt(st.nextToken());
		
		boolean[] check = new boolean[V+1];
		
		int[] dist = new int[V+1];
		Arrays.fill(dist, Integer.MAX_VALUE);
		dist[start] = 0;
		
		Queue<int[]> pq = new PriorityQueue<int[]>((o1, o2) -> o1[1]-o2[1]);
		pq.offer(new int[] {start, dist[start]});
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
		
		System.out.println(dist[dest]);
	

	}

}
