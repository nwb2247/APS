import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		
		// 아이디어 : 거꾸로 내려가면서, 지금 이 수가 다음 수들의 오큰수가 될 수 있는지 확인한다.
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		Stack<Integer> originStack = new Stack<>(); // 원래 배열을 넣는 스택 (거꾸로 인출하기 위함)
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for (int i=0; i<N; i++) {
			originStack.add(Integer.parseInt(st.nextToken()));
		}
		
		Stack<Integer> orderedStack = new Stack<>(); // 오큰수가 peek(top)에 있도록 하는 스택
		Stack<Integer> outputStack = new Stack<>();	// output String을 만들기 위한 스택
		
		while(!originStack.isEmpty()) {
			
			int cur = originStack.pop();
			
			if (orderedStack.isEmpty()) { 					// orderedStack가 비어있다면(ex) 맨 마지막 수 3 5 2 7 중 7)
				orderedStack.add(cur);						// orderedStack에 넣고 -1 리턴
				outputStack.add(-1);
			} else {
				while(!orderedStack.isEmpty()) {			// orderedStack가 비지 않았다면, (즉 오큰수 후보가 있다면)
					int bigger = orderedStack.peek();		// 제거하지 않고 꺼내서
					if (bigger > cur) {						// 나의 오큰수가 맞다면
						orderedStack.add(cur);				// 오큰수를 리턴하고, 나를 orderedStack에 추가
						outputStack.add(bigger);
						break;
					} else {								// 올바른 오큰수 나올 때까지 pop
						orderedStack.pop();
					}
				}
				
				if (orderedStack.isEmpty()) {				// 오큰수가 안나오면 -1 리턴
					outputStack.add(-1);
				}
				
				orderedStack.add(cur);						// 나를 push
				
			}
		}
		
		StringBuilder sb = new StringBuilder();
		while(!outputStack.isEmpty()) {
			sb.append(outputStack.pop() + " ");
		}
		
		System.out.println(sb);

	}

}
