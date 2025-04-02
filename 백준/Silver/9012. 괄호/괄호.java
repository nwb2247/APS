import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		StringBuilder sb = new StringBuilder();
		
		outer : 
		for (int n=1; n<=N; n++) {
			
			Stack<Character> s = new Stack<Character>();
			
			char[] chars = br.readLine().toCharArray();
			
			for(char t : chars) {
				if (t == '(') { // '('라면 push
					s.push(t);
				} else { // ')'
					if (s.isEmpty()) { // (가 있어야 하는데 없다면 No
						sb.append("NO\n");
						continue outer;
					} else {
						s.pop();

					}
				}
			}
			
			if (s.isEmpty()) {
				sb.append("YES\n");
			} else { // if s has more ")"
				sb.append("NO\n");
			}
			
		}
		
		System.out.println(sb);

	}

}
