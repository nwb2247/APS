import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		HashSet<String> map = new HashSet<>();
		for (int i=0; i<N; i++) {
			map.add(br.readLine());
		}
		
		ArrayList<String> l = new ArrayList<>();
		for (int i=0; i<M; i++) {
			String s = br.readLine();
			if (map.contains(s)) {
				l.add(s);
			}
		}
		l.sort(Comparator.naturalOrder());
		sb.append(l.size()).append("\n");
		for (String s : l) {
			sb.append(s).append("\n");
		}
		System.out.println(sb.toString());
		
	}
    
}