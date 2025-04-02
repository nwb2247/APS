// BJ 17299 오등큰수

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		int max = 1000000;
		int[] arr = new int[N];				// 원래 배열
		int[] count = new int[max+1];		// 등장한 숫자들의 출현 횟수
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i=0; i<N; i++) {
			int num = Integer.parseInt(st.nextToken());
			arr[i] = num;
			count[num] += 1;
		}
		
		// 코딩테스트에서는 새로운 클래스를 만들 시간이 부족하므로 ArrayList나 다차원 배열등을 최대한 활용하자
		// 다차원 배열을 print해보고 싶으면 Arrays.DeepToString() 사용하자
		
		Stack<Integer> orderStack = new Stack<>(); // 오등큰수 후보, 더 높은 출현 빈도를 갖는 숫자를 저장 (빈도를 저장하는 것이 아닌)
		Stack<Integer> outputStack = new Stack<>(); // 출력을 위한 스택
		
		for (int i=N-1; i>=0; i--) {
			int num = arr[i];
			int occur = count[arr[i]];


			while(!orderStack.isEmpty()) {
				int freqNum = orderStack.peek();
				if (count[freqNum] > occur) {			// peek이 오등큰수라면
					outputStack.add(freqNum);
					break;
				} else {								// peek이 오등큰수아니라면, pop후 재진행
					orderStack.pop();
				}
			}
			
			if(orderStack.isEmpty()) {					// 내 자신이 가장 큰 수라면, -1출력
				outputStack.add(-1);
			}
			
			orderStack.add(num);						// 내 자신을 오등큰수 후보로 올려둠
			
		}
		
		StringBuilder sb = new StringBuilder();
		
		while (!outputStack.isEmpty()) {
			sb.append(outputStack.pop() + " ");
		}
		
		System.out.println(sb);
		
		
	}	
	
}
