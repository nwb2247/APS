import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] s = br.readLine().split("");

		Stack<String> stack = new Stack<String>();
		
		for (int i=s.length-1; i>=0; i -= 3) {
			
			int num = 0;
			int mul = 1;
			for (int j=i; j>= 0 && j>=i-2; j--) { // 조건식 : j>= 0 && j>=i-2 : j가 0보다 작으면 break
				num += Integer.parseInt(s[j]) * mul;
				mul *= 2;
			}
			stack.push(String.valueOf(num));
			
		}
		
		StringBuilder sb = new StringBuilder();
		
		while (!stack.isEmpty()) {
			sb.append(stack.pop());
		}
		
		System.out.println(sb);
		
	}
}