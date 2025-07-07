import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		List<Integer> l = new ArrayList<>();
		
		st = new StringTokenizer(br.readLine());
		for (int i=0; i<N; i++) {
			l.add(Integer.parseInt(st.nextToken()));
		}
		
		l.sort((o1, o2) -> {
			return Math.abs(o2)-Math.abs(o1);
		});
		
//		System.out.println(l);
		
		int min = Integer.MAX_VALUE;
		List<Integer> sol = new ArrayList<>();
		for (int i=0; i<N-1; i++) {
			int abs = Math.abs(l.get(i)+l.get(i+1));
			if (abs < min) {
				min = abs;
				sol = new ArrayList<>();
				sol.add(l.get(i));
				sol.add(l.get(i+1));
				sol.sort(Comparator.naturalOrder());
			}
		}
		
		System.out.println(sol.get(0) + " " + sol.get(1));
	}
	
}
