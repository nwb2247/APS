import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		ArrayDeque<Integer> q = new ArrayDeque<>();
		
		for (int i=1; i<=N; i++) {
			q.offerLast(i);
		}
		
		while (q.size() != 1) {
			q.pollFirst();
			q.offerLast(q.pollFirst());
		}
		
		System.out.println(q.poll());
		
		
	}
}