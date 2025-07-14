import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
		
		ArrayList<ArrayList<Integer>> adjList = new ArrayList<>();
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
		
		ArrayDeque<Integer> q = new ArrayDeque<>();
		q.add(1);
		boolean[] visited = new boolean[N+1];
		visited[1] = true;
		int cnt = 0;
		while (!q.isEmpty()) {
			int cur = q.pollFirst();
			for (int i : adjList.get(cur)) {
				if (!visited[i]) {
					q.add(i);
					visited[i] = true;
					cnt++;
				}
			}
		}
		System.out.println(cnt);
		
		
	}
    
}