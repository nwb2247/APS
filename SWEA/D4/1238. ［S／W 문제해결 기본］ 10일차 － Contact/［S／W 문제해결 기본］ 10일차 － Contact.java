import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Solution {
	
	static int N;
	static ArrayList<HashSet<Integer>> adjList;
	static ArrayDeque<int[]> q;
	static boolean[] visited;
	
	int sol, depth;

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		for (int t=1; t<=10; t++) {
			st = new StringTokenizer(br.readLine());
			
			N = Integer.parseInt(st.nextToken());
			int start = Integer.parseInt(st.nextToken());
			adjList = new ArrayList<>();
			for (int i=0; i<=100; i++) {
				adjList.add(new HashSet<>());
			}
			q = new ArrayDeque<>();
			visited = new boolean[101];
			
			st = new StringTokenizer(br.readLine());
			while (st.hasMoreTokens()) {
				int from = Integer.parseInt(st.nextToken());
				int to = Integer.parseInt(st.nextToken());
				adjList.get(from).add(to);
			}
			
			int sol = -1;
			int max = 0;
			
			q.addFirst(new int[] {start, 0});
			
			while (!q.isEmpty()) {
				int[] node = q.pop();
				
				int v = node[0];
				int depth = node[1];
				if (depth > max) {
					sol = v;
					max = depth;
				} else if (depth == max && v > sol) {
					sol = v;
				}
				
				visited[v] = true;
				
				for (int u : adjList.get(v)) {
					if (visited[u]) continue;
					q.add(new int[] {u, depth+1});
				}	
				
			}
			
			sb.append("#").append(t).append(" ").append(sol).append("\n");
		
			
		}
		
		System.out.println(sb.toString());
		

	}

}
