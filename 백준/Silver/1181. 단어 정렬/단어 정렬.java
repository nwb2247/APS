import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(br.readLine());
		List<String> l = new ArrayList<>();
		 
		for (int i=0; i<N; i++) {
			l.add(br.readLine());
		}
		
		l.sort((o1, o2) -> {
			
			if (o1.length() != o2.length()) {
				return o1.length() - o2.length();
			} else {
				for (int i=0; i<o1.length(); i++) {
					if (o1.charAt(i) != o2.charAt(i)) {
						return o1.charAt(i) - o2.charAt(i);
					}
				}
				return 0;
			}
		});
		
		String prev = "";
		for (String s : l) {
			if (!s.equals(prev)) {
				sb.append(s).append("\n");
			}
			prev = s;
		}
		
		System.out.println(sb.toString());
		
		
		
	}
}