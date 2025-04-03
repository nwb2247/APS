import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
		
		ArrayList<ArrayList<int[]>> adjList = new ArrayList<>(N+1);
		for (int i=0; i<=N; i++) {
			adjList.add(new ArrayList<>());
		}
		
		for (int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			adjList.get(Integer.parseInt(st.nextToken()))
					.add(new int[] {
						Integer.parseInt(st.nextToken()),
						Integer.parseInt(st.nextToken())
					});
		}
		
		st = new StringTokenizer(br.readLine());
		int start = Integer.parseInt(st.nextToken());
		int dest = Integer.parseInt(st.nextToken());
		
		long[] dist = new long[N+1];
		Arrays.fill(dist, Long.MAX_VALUE);
		dist[start] = 0;
		
		boolean[] check = new boolean[N+1];
		
		int[] prev = new int[N+1];
		
		Queue<Node> pq = new PriorityQueue<>();
		pq.offer(new Node(start, dist[start]));
		while (!pq.isEmpty()) {
			Node cur = pq.poll();
			if (check[cur.V]) continue;
			check[cur.V] = true;
			if (cur.V == dest) break;
			for (int[] e : adjList.get(cur.V)) {
				int nextV = e[0];
				long nextDist = dist[cur.V] + e[1];
				if (dist[nextV] <= nextDist) continue;
				dist[nextV] = nextDist;
				pq.offer(new Node(nextV, nextDist));
				prev[nextV] = cur.V;
			}
		}
		
		sb.append(dist[dest]).append("\n");
		ArrayDeque<Integer> deq = new ArrayDeque<Integer>();
		deq.offerLast(dest);
		while(deq.getLast() != 0) {
			deq.offerLast(prev[deq.getLast()]);
		}
		deq.pollLast();
		sb.append(deq.size()).append("\n");
		while(!deq.isEmpty()) {
			sb.append(deq.pollLast()).append(" ");
		}
		
		System.out.println(sb.toString());

	}

}

class Node implements Comparable<Node> {
	
	int V;
	long dist;
	
	public Node(int end, long dist) {
		this.V = end;
		this.dist = dist;
	}

	@Override
	public int compareTo(Node o) {
		if (this.dist - o.dist > 0) {
			return 1;
		} else if (this.dist - o.dist == 0) {
			return 0;
		} else { // this.dist - o.dist < 0
			return -1;
		}
	}
	
	
	
	
}