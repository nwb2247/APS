import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	
	static class Node implements Comparable<Node> {
		
		int end;
		long dist;

		public Node(int end, long dist) {
			this.end = end;
			this.dist = dist;
		}

		@Override
		public String toString() {
			return "node [end=" + end + ", dist=" + dist + "]";
		}

		@Override
		public int compareTo(Node o) {
			return Long.compare(dist, o.dist);
		}	
		
	}
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		ArrayList<ArrayList<Node>> adjList = new ArrayList<>();
		for (int i=0; i<=N; i++) {
			adjList.add(new ArrayList<>());
		}
		
		for (int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			int d = Integer.parseInt(st.nextToken());
			// 주의 : 면접장까지의 가까운 거리를 찾는데, 면접장을 시작점으로 다익스트라 돌리므로
			// 시작점과 출발점을 거꾸로 받아야함
			adjList.get(e).add(new Node(s,d));
		}
		
		PriorityQueue<Node> pq = new PriorityQueue<>();
		long[] dist = new long[N+1];
		Arrays.fill(dist, Long.MAX_VALUE/2);
		
		st = new StringTokenizer(br.readLine());
		for (int i=0; i<K; i++) {
			int start = Integer.parseInt(st.nextToken());
			dist[start] = 0;
			pq.offer(new Node(start, dist[start]));
			
		}

		boolean[] check = new boolean[N+1];
		
		while (!pq.isEmpty()) {
			
			Node cur = pq.poll();
			if (check[cur.end]) continue;
			check[cur.end] = true;
			
			for (Node next : adjList.get(cur.end)) {
				
				long newDist = dist[cur.end] + next.dist;
				if (dist[next.end] <= newDist) continue;
				dist[next.end] = newDist;
				pq.offer(new Node(next.end, newDist));
			}
			
		}			

		
		int num = 0;
		long max = 0;
		
		for (int i=1; i<=N; i++) {
			if (dist[i] > max) {
				num = i;
				max = dist[i];
			}
		}
		
		
		System.out.println(num);
		System.out.println(max);

		
	}
}

