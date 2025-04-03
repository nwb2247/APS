import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

/*
 * 우선 순위 큐를 이용한 다익스트라
 * 
 * 다익스트라 : 한 정점(K)에서 다른 모든 정점으로의 최단 경로를 구하기 위한 그리디 알고리즘
 * 사용 조건 : 음수 가중치 x
 * 
 * 설명 :
 * 현재까지 방문한 정점(최단 거리가 확정된) 정점들과 연결된 정점들 중에서 
 * 아직 방문하지 않은(최단 거리가 확정되지 않은) 정점들 중 K로부터 최소 비용으로 도달가능한 정점 선택, 방문(최단 거리 확정)
 * => 그리디 알고리즘 : 매 순간 K로부터 최소 비용으로 도달가능한 정점을 찾고 업데이트하면,
 * 	 			   K로부터 모든 정점까지의 최단 경로를 구할 수 있다. 
 * 
 * 최소 비용 뿐만 아니라, 경로 자체를 구하고 있으면 prev[] 배열을 사용
 *
 * ---------------------------------------------------------------------------
 * 
 * 참고) 그래프 관련 알고리즘
 * 
 * 
 * ● 최단 경로 알고리즘(Shortest Path Problem)
 * 
 * 플로이드 워셜: 모든 정점 쌍 간 최단 거리 구하는 알고리즘 (음수인 가중치 OK, but 음수 사이클 X)
 * 
 * 벨만 포드 	: 다익스트라와 비슷하나 음수 가중치 OK,  (코테엔 잘 나오지 않음)
 * 			  아직 방문 안한 정점들에서 최단 경로를 찾는 다익스트라와 달리 벨만 포드는 매 단계 모든 간선을 전부 확인
 * 			  다익스트라보다 느리고 플로이드 워셜보다 빠름
 * 
 * A*		: 정점의 개수가 너무 많아 다익스트라 적용 어려울 때, 근사적인 최소 거리를 찾는 알고리즘 (코테엔 잘 나오지 않음)
 * 
 * 
 * ● 최소 신장 트리(MST) 알고리즘
 * 신장 트리 : 모든 정점을 가장 적은 간선 수로 연결한 그래프
 * 최소 신장 트리 : 신장 트리 중에서 사용된 가중치이 합이 최소인 트리
 * 
 * 크루스칼 (그리디), 프림
 * 
 * 
 * ● 위상 정렬
 *  => DFS
 * 
 */	

// 인접 리스트에 간선을 표현하기 위한 클래스 정의
class Edge {
	
	int dest, cost;
	
	Edge(int dest, int cost) {
		this.dest = dest;
		this.cost = cost;
	}
	
}

// 한 정점 dest과, K에서 해당 정점 dest로 가는 비용 costSum를 저장하는 클래스 정의 (Edge와는 다름)
class CostSum implements Comparable<CostSum> {
	
	int dest, costSum;
	
	CostSum(int dest, int costSum) {
		this.dest = dest;
		this.costSum = costSum;
	}

	@Override
	public int compareTo(CostSum o) {
		// TODO Auto-generated method stub
		// this.costSum - o.costSum;을 사용하면 overflow 날 수 있으므로, 안전하게 Integer.compare로 비교
		// Integer.compare -1, 0, 1로 반환
		return Integer.compare(this.costSum, o.costSum);
	}
	
}


public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		int V = Integer.parseInt(st.nextToken());
		int E = Integer.parseInt(st.nextToken());
		
		int K = Integer.parseInt(br.readLine());
		
		// ------------------ 인접리스트 생성 ------------------ 
		ArrayList<ArrayList<Edge>> adjList = new ArrayList<>();
		for (int i=0; i<=V; i++) {
			adjList.add(new ArrayList<>());
		}
		
		// ------------------ 인접리스트 채우기 ------------------ 
		for (int i=0; i<E; i++) {
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int dest = Integer.parseInt(st.nextToken());
			int cost = Integer.parseInt(st.nextToken());
			adjList.get(start).add(new Edge(dest, cost));
		}

		// ------------------ 다익스트라 ------------------ 
		boolean[] visited = new boolean[V+1]; 	// 최단거리가 확정된 정점
		int[] costTotal = new int[V+1];			// 현재까지의 각 정점까지의 최소 비용
		Arrays.fill(costTotal, Integer.MAX_VALUE);
		costTotal[K] = 0; // 시작 지점 K로부터 K까지의 거리 : 0
		
		PriorityQueue<CostSum> pq = new PriorityQueue<>(); // 도달 가능한 남은 정점 중 최소 거리 정점를 가져오기 위해 우선순위 큐 생성
		
		pq.offer(new CostSum(K, 0)); // K부터 시작해 하나씩 순회하기 위해 costSum(K,0)생성
		
		while(!pq.isEmpty()) {
			
			int curV = pq.poll().dest;
			if (visited[curV]) continue; // 이미 최소 거리 확정된 정점은 패스
			
			visited[curV] = true;
			
			for (Edge e : adjList.get(curV)) {
				
				int nextV = e.dest;
				int newCost = costTotal[curV] + e.cost;
				if (newCost < costTotal[nextV]) {
					costTotal[nextV] = newCost;
					pq.offer(new CostSum(nextV, newCost));
				}

			}
		}
		
		// ------------------ 출력 ------------------ 
		for (int i=1; i<=V; i++) {
			if (costTotal[i] == Integer.MAX_VALUE) {
				sb.append("INF").append("\n");
			} else {
				sb.append(costTotal[i]).append("\n");
			}
		}
		
		System.out.println(sb);
		

	}

}


