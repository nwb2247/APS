// BJ2609

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int A = Integer.parseInt(st.nextToken());
		int B = Integer.parseInt(st.nextToken());
		
		int min = Math.min(A, B);
		
		int GCM;
		for (GCM=min; GCM>=1; GCM--) {
			if (A % GCM == 0 && B % GCM == 0) break;
		}
		
		int LCM = (A*B) / GCM;
		
		StringBuilder sb = new StringBuilder();
		sb.append(GCM + "\n");
		sb.append(LCM + "\n");
		System.out.println(sb);

		
	}

}
