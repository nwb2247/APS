import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		for (int t=0; t<T; t++) {
			int N = Integer.parseInt(br.readLine());
			HashMap<String, Integer> map = new HashMap<>();
			for (int i=0; i<N; i++) {
				st = new StringTokenizer(br.readLine());
				st.nextToken();
				String type = st.nextToken();
				if (!map.containsKey(type)) {
					map.put(type, 2);
				} else {
					map.put(type, map.get(type)+1);
				}
			}
			int sum = 1;
			for (int num : map.values()) {
				sum *= num;
			}
			sb.append(sum-1).append("\n");
		}
		System.out.print(sb.toString());
		
	}
    
}