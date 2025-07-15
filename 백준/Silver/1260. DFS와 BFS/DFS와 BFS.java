import java.io.*;
import java.util.*;

public class Main {
	
	static StringBuilder sb;
	static ArrayList<ArrayList<Integer>> adjList;
	static boolean[] visited;
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		sb = new StringBuilder();
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int V = Integer.parseInt(st.nextToken());
		
		adjList = new ArrayList<>();
		for (int i=0; i<=N; i++) {
			adjList.add(new ArrayList<>());
		}
		for (int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			adjList.get(s).add(e);
			adjList.get(e).add(s);
		}
		for (int i=0; i<=N; i++) {
			adjList.get(i).sort(Comparator.naturalOrder());
		}
		
		visited = new boolean[N+1];
		sb.append(V).append(" ");
		visited[V] = true;
		doDFS(V);
		sb.append("\n");
		
		ArrayDeque<Integer> q = new ArrayDeque<>();
		q.addLast(V);
		Arrays.fill(visited, false);
		visited[V] = true;
		while (!q.isEmpty()) {
			int cur = q.pollFirst();
			sb.append(cur).append(" ");
			for (int i : adjList.get(cur)) {
				if (visited[i]) continue;
				q.addLast(i);
				visited[i] = true;
			}
		}
		
		System.out.println(sb.toString());
		
	}
	
	public static void doDFS(int v) {
		
		for (int i : adjList.get(v)) {
			if (visited[i]) continue;
			sb.append(i).append(" ");
			visited[i] = true;
			doDFS(i);
		}
		
	}
    
}

