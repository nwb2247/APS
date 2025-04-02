import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Main {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		int[] evens = new int[T];
		
		for (int t=0; t<T; t++) {
			evens[t] = Integer.parseInt(br.readLine());
		}
		
		// int[] 배열에 최대값을 찾기 위한 방법 : Arrays.stream 메서드 사용
		
		int max = Arrays.stream(evens).max().orElse(0);
		// orElse(0); 배열이 비어있을 경우 어떤 값을 리턴할지 결정해야 함
		
		List<Integer> list = new ArrayList<>();
		Set<Integer> set = new HashSet<>();
		
		boolean[] notPrime = new boolean[max+1];
		
		notPrime[0] = true;
		notPrime[1] = true;
		
		for (int i=2; i<=max; i++) {
			
			if (notPrime[i]) { // 합성수라면 패스
				continue;
			}
			list.add(i);
			set.add(i); // 소수라면 set, list에 추가
			for (int j=i+i; j<=max; j += i) {
				notPrime[j] = true;
			}
		}
		
		StringBuilder sb = new StringBuilder();
		
		for (int N : evens) {
			int count = 0;
			for (int i=0; i<list.size() && list.get(i) <= N/2; i++) { // 순서가 같은 것은 하나로 치므로 N/2까지만 탐색
				if (set.contains(N-list.get(i))) {
					count++;
				}
			}
			sb.append(count+"\n");
		}
		
		System.out.println(sb);
		
		

	}

}
