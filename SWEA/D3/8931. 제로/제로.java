import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Solution {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		for (int t=1; t<=T; t++) {
			
			int K = Integer.parseInt(br.readLine());
			
			Stack<Integer> stack = new Stack<>();
			
			int sum = 0;
			for (int i=0; i<K; i++) {
				
				int N = Integer.parseInt(br.readLine());
				if (N == 0) {
					stack.pop(); // 문제에서 정수가 0일 경우 지울 수 있는 수가 있음이 보장되어있으므로, isEmpty()수행 필요 x
				} else {
					stack.push(N);
				}
				
			}
			
			while(!stack.isEmpty()) {
				sum += stack.pop();
			}
			
			System.out.println("#"+t+" "+sum);
			
			
		}
		
	}

}
