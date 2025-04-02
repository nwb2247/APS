import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws Exception{
		
		List<Integer> deque = new LinkedList<Integer>();
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		StringBuilder sb = new StringBuilder();

		
		for (int i=1; i<=N; i++) {
			
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			String op = st.nextToken();
			int X = 0;
			if (st.hasMoreTokens()) X = Integer.parseInt(st.nextToken());
			
			switch(op) {
			case "push_front" :
				deque.add(0, X); // 맨 앞에 추가
				break;
			case "push_back":
				deque.add(X); // 인덱스 부여 안하면. 맨뒤에 추가
				break;
			case "pop_front":
				if (deque.size() == 0) {
					sb.append(-1 + "\n");
					break;
				}
				sb.append(deque.remove(0) + "\n"); // 맨 앞 제거
				break;
			case "pop_back":
				if (deque.size() == 0) {
					sb.append(-1 + "\n");
					break;
				}
				sb.append(deque.remove(deque.size()-1) + "\n"); // 맨뒤 제거
				break;
			case "size":
				sb.append(deque.size() + "\n");
				break;
			case "empty":
				if (deque.size() == 0) {
					sb.append(1 + "\n");
				} else {
					sb.append(0 + "\n");
				}
				break;
			case "front":
				if (deque.size() == 0) {
					sb.append(-1 + "\n");
					break;
				}
				sb.append(deque.get(0) + "\n");
				break;
			case "back":
				if (deque.size() == 0) {
					sb.append(-1 + "\n");
					break;
				}
				sb.append(deque.get(deque.size()-1) + "\n");
				break;
			}
			
		}
		
		System.out.println(sb);

	}

}
