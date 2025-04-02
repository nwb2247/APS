import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int N, M;
	static ArrayList<ArrayList<Integer>> adjList; 
	
	static boolean[] visited;
	
	static boolean sol = false;

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		adjList = new ArrayList<>();
		for (int i=0; i<N; i++) {
			adjList.add(new ArrayList<>());
		}
		
		visited = new boolean[N];	
		
		for (int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			int u = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			adjList.get(u).add(v);
			adjList.get(v).add(u);
		}
		
		for (int i=0; i<N; i++) {
			Arrays.fill(visited, false);
			if (BT(i, 1)) {
				System.out.println(1);
				return;
			}
		}
		
		System.out.println(0);
		

	}
	
	private static boolean BT(int v, int depth) {
		
		if (depth == 5) {
			return true;
		}

//		System.out.println(adjList.get(v));
//		System.out.println(Arrays.toString(visited));
		
		visited[v] = true;
		for (int u : adjList.get(v)) {
			if (visited[u]) continue;
			if (BT(u, depth+1)) {
				return true;
			}
		}
		visited[v] = false;
		
		return false;
		
	}

}
