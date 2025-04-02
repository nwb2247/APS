import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
	
	static int T;
	static int N, M;
	static int[] incom; 	// incompatible : incom[1] : 1과 양립불가능한 재료를 비트기준으로 표현하여 저장
	static int cnt;

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		T = Integer.parseInt(br.readLine());
		
		for (int t=1; t<=T; t++) {
			 
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			
			incom = new int[N+1];
			Arrays.fill(incom, 1<<N);
			for (int i=0; i<M; i++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				// 재료 1 ~ N : 0 ~ N-1번째 bit에 해당 
				// bit합 연산을 통해 a, b와 양립불가능한 재료 정보를 저장
				incom[a] = incom[a] | 1<<(b-1); 			
				incom[b] = incom[b] | 1<<(a-1);
			}
			
//			System.out.println(Arrays.toString(incom));
			
			// 공집합(아무 재료도 안들어가는 경우)는 항상 포함이므로 1부터 시작
			cnt = 1;
			subset(0, 1<<N); // 0을 넣어야 1부터 순회
			sb.append("#")
			  .append(t)
			  .append(" ")
			  .append(cnt)
			  .append("\n");

		}
		
		System.out.println(sb);

		
	}
	
	public static void subset(int startIdx, int notAvail) {
		
		if (startIdx > N) { // 모든 재료의 추가 여부를 다 결정했으면 종료
			return;
		}
		
		// 조합 생성방식과 마찬가지로 다음 인덱스(i=startIdx+1)부터 추가
		for (int i=startIdx+1; i<=N; i++) {
			if ((notAvail & 1<<i-1) == 0) { // 해당 재료가 추가가능하다면
				cnt++;
//				System.out.println(i + " " + (notAvail | incom[i]));
				subset(i, notAvail | incom[i]); // 새로 추가한 재료를 고려해 추가 불가능한 재료를 업데이트함
			}
		}
		
		
		
		
	}

}
