import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		List<int[]> l = new ArrayList<>();
		
		int N = Integer.parseInt(br.readLine());
		
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			l.add(new int[] {Integer.parseInt(st.nextToken()),
								Integer.parseInt(st.nextToken())});
		}
		
		l.sort((o1, o2) -> {
			if (o1[1] != o2[1]) {
				return Integer.compare(o1[1], o2[1]);
			} else {
				if (o1[0] != o2[0]) {
					return Integer.compare(o1[0], o2[0]);
				}
			}
			return 0;
		});
		
		ArrayDeque<int[]> opt = new ArrayDeque<>();
		opt.add(new int[] {0,0});
		
		for (int[] e : l) {
//			System.out.println(e[0] + " " + e[1]);
			if (opt.peekLast()[1] <= e[0]) {
				opt.offerLast(e);
			}
		}
		
//		for (int[] e : opt) {
//			System.out.println(e[0] + " " + e[1]);
//		}
		
		System.out.println(opt.size()-1);
		
		
		
		
		
	}
}