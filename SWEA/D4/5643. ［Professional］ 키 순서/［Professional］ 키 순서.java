import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {
	
	static int N, M;
	static ArrayList<ArrayList<Integer>> shorter;
	static ArrayList<ArrayList<Integer>> taller;
	
	static int[] cntShorter, cntTaller;
		
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		for (int tc=1; tc<=T; tc++) {
			N = Integer.parseInt(br.readLine());
			M = Integer.parseInt(br.readLine());
			
			shorter = new ArrayList<>();
			taller = new ArrayList<>();
			for (int i=0; i<=N; i++) { 			// 1~N
				shorter.add(new ArrayList<>());
				taller.add(new ArrayList<>());
			}	
			
			for (int i=0; i<M; i++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				
				shorter.get(b).add(a); 	// b 보다 a가 작다.
				taller.get(a).add(b);	// a 보다 b가 크다.
				
			}
			
			cntShorter = new int[N+1];			// 1~N
			cntTaller = new int[N+1];	
			
			// taller
			for (int i=1; i<=N; i++) {
				
				Queue<Integer> q = new ArrayDeque<>();
				boolean[] visited = new boolean[N+1];
				
				q.add(i);
				visited[i] = true;
				
				while (!q.isEmpty()) {
					int cur = q.poll();
					
					for (int s : shorter.get(cur)) {
						if (visited[s]) continue;
						visited[s] = true;
						cntShorter[i]++; 
						q.add(s);
					}
				}
			}
			
			// taller
			for (int i=1; i<=N; i++) {
				
				Queue<Integer> q = new ArrayDeque<>();
				boolean[] visited = new boolean[N+1];
				
				q.add(i);
				visited[i] = true;
				
				while (!q.isEmpty()) {
					int cur = q.poll();
					
					for (int t : taller.get(cur)) {
						if (visited[t]) continue;
						visited[t] = true;
						cntTaller[i]++; 
						q.add(t);
					}
				}
			}
			
			int sol = 0;
			for (int i=1; i<=N; i++) {
				if (cntShorter[i] + cntTaller[i] != N-1) continue;
				sol++;
			}
			
			sb.append("#").append(tc).append(" ").append(sol).append("\n");
			
		}
		
		System.out.println(sb.toString());
		
		
	}

}
