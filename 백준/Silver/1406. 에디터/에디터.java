import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();		
		
		// 커서는 맨끝에서부터 시작하므로, llist이 왼쪽 stack이 오른쪽 부분
		LinkedList<Character> llist = new LinkedList<Character>(); //커서의 왼쪽 부분
		for (char c : str.toCharArray()) {
			llist.addLast(c); // 맨 뒤에 추가 ( 맨 앞은 push())
		}
		Stack<Character> stack = new Stack<Character>(); //커서의 오른쪽 부분
		
		int M = Integer.parseInt(br.readLine());
		
		for (int m=1; m<=M; m++) {
			
			StringTokenizer st = new StringTokenizer(br.readLine());
			Character op = st.nextToken().toCharArray()[0];
			
			switch(op) {
			case 'P':
				Character $ = st.nextToken().toCharArray()[0];
				llist.addLast($); //
				break;
			case 'L': // 커서를 왼쪽으로 -> llist에서 pop last해서 stack에 push
				if (!llist.isEmpty()) stack.push(llist.removeLast()); // 
				break;
			case 'D': // 커서를 오른쪽으로
				if (!stack.isEmpty()) llist.addLast(stack.pop());
				break;
			case 'B':
				if (!llist.isEmpty()) llist.removeLast();
				break;
			} // defualt는 선택사항이므로 안한다고 컴파일 에러가 뜨지는 않음	
			
		}
		
		StringBuilder sb = new StringBuilder();
		while(!llist.isEmpty()) {
			sb.append(llist.removeFirst());
		}
		while(!stack.isEmpty()) {
			sb.append(stack.pop());
		}
		System.out.println(sb);
		
		
	}

}
