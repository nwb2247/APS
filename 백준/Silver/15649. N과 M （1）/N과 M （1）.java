import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		boolean[] visited = new boolean[N];
		int[] output = new int[M];
		
		StringBuilder sb = new StringBuilder();
		
		permute(visited, 0, output, N, M, sb);
		
		System.out.println(sb);
		
	}
	
	public static void permute(boolean[] visited, int depth, int[] output, int N, int M, StringBuilder sb) {
		
		if (depth == M) {
			for (int i : output) {
				sb.append(i+1 + " ");
			}
			sb.append("\n");
			return;
		}
		
		for (int i=0; i<N; i++) {
			if (!visited[i]) {
				
				output[depth] = i;
				visited[i] = true;
				
				permute(visited, depth+1, output, N, M, sb);
				
				visited[i] = false;
			}
		}
		
		
	}
	
}

