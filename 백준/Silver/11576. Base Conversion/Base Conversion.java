import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		
		int A = Integer.parseInt(st.nextToken());
		int B = Integer.parseInt(st.nextToken());
		
		int size = Integer.parseInt(br.readLine());
		
		int N = 0;
		
		st = new StringTokenizer(br.readLine());
		for (int i=0; i<size; i++) {
			N = N*A + Integer.parseInt(st.nextToken());
		}
		
//		System.out.println(N);
		
		Stack<String> stack = new Stack<>();
		
		int Q = N;
		int R;
		
		while (true) {
			R = Q%B;
			Q = Q/B;
			
			stack.add(String.valueOf(R));
			if (Q == 0) break;
		}
		
		StringBuilder sb = new StringBuilder();
		
		while (!stack.empty()) {
			sb.append(stack.pop() + " ");
		}
		System.out.println(sb.toString().strip());
		// 스택을 사용하지 않고, sb.reverse 돌리면, 모든 문자열이 뒤집힌다.
		// 예시
		// 16 16 / 2 / 15 15 입력하면
		// 15 15가 나와야하나, 51 51이 나옴

	}

}
