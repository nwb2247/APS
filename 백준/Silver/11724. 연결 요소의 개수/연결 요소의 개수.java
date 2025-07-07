import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		List<List<Integer>> adjList = new ArrayList<>();
		for (int i=0; i<=N; i++) {
			adjList.add(new ArrayList<>());
		}
		
		for (int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			int u = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			adjList.get(u).add(v);
			adjList.get(v).add(u);
		}
		
		boolean[] visited = new boolean[N+1];
		Queue<Integer> q = new ArrayDeque<>();
		
		int cnt = 0;
		for (int i=1; i<=N; i++) {
			if (visited[i]) continue;
			cnt++;
			q.offer(i);
			visited[i] = true;
			while(!q.isEmpty()) {
				int cur = q.poll();
				for (int next : adjList.get(cur)) {
					if (visited[next]) continue;
					visited[next] = true;
					q.offer(next);
				}
			}
		}
		
		System.out.println(cnt);
				
	}

}
