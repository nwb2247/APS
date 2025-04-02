import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

public class Main {

	public static void main(String[] args) throws Exception {
		int max = 1000000;
		
		boolean[] prime = new boolean[max+1];
		Arrays.fill(prime, true);
		prime[0] = false;
		prime[1] = false;
		
		ArrayList<Integer> primeOL = new ArrayList<Integer>(); // 작은 순서대로 a를 결정하기 위한 ordered list;
		HashSet<Integer> primeSet = new HashSet<Integer>(); // b를 찾기 위한 Set
		
		for (int i=2; i<=max; i++) {
			if (!prime[i]) continue;
			
			primeOL.add(i);
			primeSet.add(i);
			for (int j=i+i; j<=max; j += i) {
				prime[j] = false;
			}
		}
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int n;
		while ((n = Integer.parseInt(br.readLine())) != 0) {
			
			boolean found = false;
			for (int a : primeOL) {
				int b = n-a;
				if (primeSet.contains(b)) {
					found = true;
					sb.append(n + " = " + a + " + " + b + "\n");
					break;
				}
			}
			
			if (found == false) sb.append("Goldbach's conjecture is wrong.");
			
		}
		
		System.out.println(sb);

	}

}
