import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		int M = Math.max(N, 2*K);
		
		int[][] graph = new int[M+1][3];
		boolean[] visited = new boolean[M+1];
		int[] before = new int[M+1];
		
		for (int i=0; i<=M; i++) {
			
			graph[i][0] = (i-1 < 0)? -1 : i-1;
			graph[i][1] = (i+1 > M)? -1 : i+1;
			graph[i][2] = (2*i > M)? -1 : 2*i;

		}
		
		// BFS
		
		Queue<Integer> queue = new ArrayDeque<>();
		
		queue.add(N);
		visited[N] = true;
		
		while (!queue.isEmpty()) {
			
			int node = queue.poll();
			
			
			if (node == K) {
				break;
			}
			
			for (int i=0; i<3; i++) {
				int next = graph[node][i];
				
				if (next == -1 || visited[next]) continue;
				
				// 큐에 추가
				queue.add(next);
				visited[next] = true;
				before[next] = node;				
				
			}
		}
		
		Deque<Integer> stack = new ArrayDeque<>();
		
		stack.addLast(K);
		while (stack.getLast() != N) {
			stack.addLast(before[stack.getLast()]);
		}
		
		StringBuilder sb = new StringBuilder();
		sb.append(stack.size()-1);
		sb.append("\n");
		while (!stack.isEmpty()) {
			sb.append(stack.removeLast() + " ");
		}
		
		System.out.println(sb);
		
		

	}

}
