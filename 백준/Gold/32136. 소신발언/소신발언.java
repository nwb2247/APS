import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static long[] frozen;
	static int N;
	
	public static void main(String[] args) throws IOException {
		
		// 녹이는 방법 중 최솟값은 무엇인가? 라는 최적화 문제를 X시간에 녹이는 것이 가능한가? 라는 결정문제로 바꾸어 푼다.
		// 파라메트릭 서치

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		
		StringTokenizer st = new StringTokenizer(br.readLine());

		frozen = new long[N];
		
		for (int i=0; i<N; i++) {
			frozen[i] = Integer.parseInt(st.nextToken());
		}
		
		long minTime = 0; // 최솟값을 찾기 위해 파라메트릭 서치를 적용할 때, 현재 범위중 가장 작은 time을 의미
		long maxTime = 500000L*N; // 최솟값을 찾기 위해 파라메트릭 서치를 적용할 때, 현재 범위중 가장 큰 time을 의미 (언 정도의 최대치 500000)
		// 실제 최솟값은 midTime으로 반환될 예정
		
		long result = 0;
		while(minTime <= maxTime) {
			
			long midTime = (minTime+maxTime)/2;
			
			if (check(midTime)) {
				result = midTime; // 정답의 후보이므로 result에 저장
				maxTime = midTime-1;
			} else {
				minTime = midTime+1;
			}
			
		}
		
		System.out.println(result);
		
		
		

	}
	
	public static boolean check(long time) { // time시간 내에 녹일 방법(히터를 놓을 수 있는 범위)이 있는가?
		
		long left = 0; // binary search의 left right가 아닌, 히터를 둘 수 있는 범위를 의미함.
		long right = N-1;
		
		for (int i=0; i<N; i++) {
			long dist = time / frozen[i]; 
			/*
			 * ex) 언 정도가 5 이고 2초안에 녹이려면? 히터가 5/2 => 2거리 안에 있어야함(나누어 떨어지는 경우도 동일)
			 * 		=> 현재 위치 i가 3이라면 1~5까지 가능
			 */
			left = Math.max(left, i-dist);
			right = Math.min(right, i+dist);
			
			if (left > right) { // 히터를 둘 수 있는 범위가 없다면 false 반환;
				return false;
			}
		}
		
		return true; //히터를 둘 수 있는 범위가 있으므로 true 반환;
	}
	

}
