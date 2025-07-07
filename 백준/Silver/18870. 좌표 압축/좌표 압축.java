import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(br.readLine());
		
		st = new StringTokenizer(br.readLine());
		
		int[] arr = new int[N];
		Set<Integer> s = new HashSet<>();
		
		for (int i=0; i<N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
			s.add(arr[i]);
		}
		
		List<Integer> l = new ArrayList<>();
		for (int e : s) {
			l.add(e);
		}
		l.sort(Comparator.naturalOrder());
		
		Map<Integer, Integer> m = new HashMap<>();
		for (int i=0; i<l.size(); i++) {
			m.put(l.get(i), i);
		}
		
		for (int e : arr) {
			sb.append(m.get(e)).append(" ");
		}
		
		System.out.println(sb.toString());

		
	}
}
