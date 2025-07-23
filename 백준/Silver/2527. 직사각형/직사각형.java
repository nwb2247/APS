import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		StringBuilder sb = new StringBuilder();
		
		for (int t=0; t<4; t++) {
			st = new StringTokenizer(br.readLine());
			
			int[] first = new int[4];
			int[] second = new int[4];
			
			for (int i=0; i<4; i++) {
				first[i] = Integer.parseInt(st.nextToken());
			}
			for (int i=0; i<4; i++) {
				second[i] = Integer.parseInt(st.nextToken());
			}
			
			if (first[0] == first[2] && // 직사각형이 이미 아닌 경우
					first[1] == first[3] &&
					second[0] == second[2] &&
					second[1] == second[3]) {
				sb.append("d\n");
			} else if ((first[0] == second[2] && first[1] == second[3]) || // 점끼리 겹치는 경우
					(first[2] == second[0] && first[1] == second[3]) ||
					(first[0] == second[2] && first[3] == second[1]) ||
					(first[2] == second[0] && first[3] == second[1])) {
				sb.append("c\n");	
			} else if (first[2] < second[0] || second[2] < first[0] || // 아무것도 겹치지 않는 경우
					first[3] < second[1] || second[3] < first[1]) {
				sb.append("d\n");
			} else if (first[0] == second[2] ||	// 점겹침도 아니고, 아무것도 안겹치는게 아니라면, 해당 조건에서는 변끼리 겹치게 된다.
					first[2] == second[0] ||
					first[1] == second[3] ||
					first[3] == second[1]) {
				sb.append("b\n");
			} else {	// 직사각형 범위로 겹치는 경우
				sb.append("a\n");
			}
			
			// 분기를 정확한 순서로 하는 것이 중요함...
			
		}
		
		System.out.println(sb.toString().trim());
		

	}

}
