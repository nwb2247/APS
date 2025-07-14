import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		String[] NtoS = new String[N+1];
		HashMap<String, Integer> StoN = new HashMap<>();
		for (int i=1; i<=N; i++) {
			NtoS[i] = br.readLine();
			StoN.put(NtoS[i], i);
		}
		for (int i=0; i<M; i++) {
			String input = br.readLine();
			Integer output = StoN.get(input);
			if (output == null) {
				sb.append(NtoS[Integer.parseInt(input)]);
			} else {
				sb.append(output);
			}
			sb.append("\n");
		}
		System.out.println(sb.toString());
		
	}
    
}