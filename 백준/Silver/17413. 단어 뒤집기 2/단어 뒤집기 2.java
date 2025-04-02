// BJ 17413
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class Main {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		char[] chars = br.readLine().toCharArray();
		
		Stack<Character> stack = new Stack<>(); // 꺽쇠 밖
		Queue<Character> queue = new LinkedList<>(); // 꺽쇠 안
		
		StringBuilder sb = new StringBuilder();
		
		boolean isStackState = true; // false면 queue 상태 (즉, queue에서 push pop하는 상태)
		for (char c : chars) {
			if (c == '<') { 						// < 만나면 기존의 s,q모두 flush하고 q상태로 바꿈
				if (isStackState) {
					while (!stack.isEmpty()) {
						sb.append(stack.pop());
					}
				} else {
					while (!queue.isEmpty()) {
						sb.append(queue.remove());
					}
				}
				isStackState = false;
				queue.add(c);
			} else if (c == '>') {					// > 만나면 q상태였을 것이므로 flush하고 s상태로 바꿈
				while(!queue.isEmpty()) {
					sb.append(queue.remove());
				}
				sb.append(c);
				isStackState = true;
			} else if (c == ' ') {					// 공백 만나면 q, s 상태에 따라 모두 flush
				if (isStackState) {
					while (!stack.isEmpty()) {
						sb.append(stack.pop());
					}
				} else {
					while (!queue.isEmpty()) {
						sb.append(queue.remove());
					}
				}
				sb.append(c);
			} else {								// 그 외 일반 문자열은 q, s 상태에 따라 모두 push
				if (isStackState) {
					stack.add(c);
				} else {
					queue.add(c);
				}
			}
		}
		
		if (isStackState) {							// 모든 문자에 대해 진행되었을때, 남은 것들을 s,q 에 따라 flush
			while (!stack.isEmpty()) {
				sb.append(stack.pop());
			}
		} else {
			while (!queue.isEmpty()) {
				sb.append(queue.remove());
			}
		}
		
		System.out.println(sb);
		
		

	}

}
