import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.StringTokenizer;

// 최소신장트리 (크루스칼 - 연결그래프)

class Edge implements Comparable<Edge>{
	
	int start, end, cost;
	
	Edge(int start, int end, int cost) {
		this.start = start;
		this.end = end;
		this.cost = cost;
	}

	@Override
	public String toString() {
		return "Edge [start=" + start + ", end=" + end + ", cost=" + cost + "]";
	}
	
	@Override
	public int compareTo(Edge o) {
		// TODO Auto-generated method stub
		return Integer.compare(this.cost, o.cost);
	}
	
}

public class Main {

	static int V, E;
	
	/* - 크루스칼, (간선의 가중치 기준으로 정렬하고 작은 것부터 추가할 것이므로 adjList는 필요 없음)
	 * 연결 그래프라면 MST 완성시 간선의 수 cnt == V-1개 됨
	 * 비연결 그래프라면 간선의 수 cnt가 V-1에 도달하지 못하고, 모든 간선의 수(E)만큼 for문을 돌게됨.
	 * 그 결과로 MSF(Minimum Spanning forest)가 완성됨
	 */
	static ArrayList<Edge> edges;
	static int cnt;
	static int[] prev;
	static int costTotal;
	
	// 유니온 파인드
	static int[] root;
	static int[] rank;

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		V = Integer.parseInt(st.nextToken());
		E = Integer.parseInt(st.nextToken());
		
		// 크루스칼
		edges = new ArrayList<>();
		cnt = 0;
		prev = new int[V];
		costTotal = 0;
		
		// 유니온 파인드
		root = new int[V];
		rank = new int[V];
		for (int i=0; i<V; i++) {
			root[i] = i;
			rank[i] = 1;
		}
		
		for (int i=0; i<E; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			edges.add(new Edge(a, b, c));			
		}
		
		Collections.sort(edges);
		
		
		for (Edge edge : edges) {
			// 넣으려고 할 때 이미 양쪽이 같은 집합에 있다면, 추가시에 사이클 발생하므로 포함하면 안됨
			// union 메서드가 양쪽이 같은 집합이라면 false 반환하므로 아래와 같이 조건 확인
			if (union(edge.start-1, edge.end-1)) {
				costTotal += edge.cost;
			}
		}
		
		System.out.println(costTotal);


	}
	
	static int find(int x) {
		
		if (root[x] == x) {
			return x;
		}
		
		return root[x] = find(root[x]);
	}
	
	static boolean union(int a, int b) {
		
		int u = find(a);
		int v = find(b);
		
		if (u == v) return false; // 같으면 false
		
		if (rank[v] > rank[u]) {
			int temp = u;
			u = v;
			v = temp;
		}
		
		if (rank[u] == rank[v]) {
			rank[u]++;
		}
			
		root[v] = u;
		return true;
		
	}

}




























