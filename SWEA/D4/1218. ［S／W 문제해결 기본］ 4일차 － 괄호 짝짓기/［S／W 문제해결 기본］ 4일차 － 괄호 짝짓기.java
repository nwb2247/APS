import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Solution {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		for (int t=1; t<=10; t++) {
			int N = Integer.parseInt(br.readLine());
			char[] arr = br.readLine().toCharArray();
			
			Stack<Character> stack = new Stack<>();
			
			int sol = 1;
			
			outer : 
			for (int i=0; i<N; i++) {
				switch(arr[i]) {
				case '(' :
				case '{' :
				case '[' :
				case '<' :
					stack.push(arr[i]);
					break;
				case ')' :
					if (stack.isEmpty()) {
						sol = 0;
						break outer;
					} else if (stack.pop() != '(') {
						sol = 0;
						break outer;
					}
					break;
				case '}' :
					if (stack.isEmpty()) {
						sol = 0;
						break outer;
					} else if (stack.pop() != '{') {
						sol = 0;
						break outer;
					}
					break;
				case ']' :
					if (stack.isEmpty()) {
						sol = 0;
						break outer;
					} else if (stack.pop() != '[') {
						sol = 0;
						break outer;
					}
					break;
				case '>' :
					if (stack.isEmpty()) {
						sol = 0;
						break outer;
					} else if (stack.pop() != '<') {
						sol = 0;
						break outer;
					}
					break;
				}
			}
			
			if (!stack.isEmpty()) {
				sol = 0;
			}
			
			System.out.println("#"+t+" "+sol);
			
		}

	}

}
