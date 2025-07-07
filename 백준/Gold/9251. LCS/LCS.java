import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		char[] input1 = br.readLine().toCharArray();
		char[] input2 = br.readLine().toCharArray();
		
		int[][] DP = new int[input1.length + 1][input2.length + 1];
		
		for (int i=1; i<=input1.length; i++) {
			for (int j=1; j<=input2.length; j++) {
				DP[i][j] = Math.max(DP[i-1][j], DP[i][j-1]);
				if (input1[i-1] == input2[j-1]) {
					DP[i][j] = DP[i-1][j-1]+1;
				}
			}
		}
		
//		System.out.println(Arrays.deepToString(DP));
		System.out.println(DP[input1.length][input2.length]);
		
	}
	
	/*
	 *   CAPCAK
	 *  0000000
	 * A0011111
	 * C0111222
	 * A0122233
	 * Y0122233
	 * K0122234
	 * P0123334
	 * 
	 * input1[a]와 input2[b]를 비교했을때,
	 * 다르다면 
	 * 		input1의 a-1까지와 input2의 b까지 비교했을 때의 LCS의 길이
	 * 		input1의 a까지와 input2의 b-1까지 비교했을 떄의 LCS의 길이
	 * 		중 큰 것을 그대로 가져오면 됨.
	 * 같다면
	 * 		input1의 a-1까지와 input2의 b-1까지 비교했을 떄의 LCS+1가 LCS가 됨.
	 * 
	 * 빈 문자열과의 비교를 위해 DP의 인덱스는 1부터 시작하게 하도록 함
	 * 
	 * 이중for문을 통해 차례대로 각 i, j에 대한 DP값을 순차적으로 빈틈없이 구해나갈 수 있음
	 * (DP[i][j]가 오롯이 DP[i-1][j] DP[i][j-1] DP[i-1][j-1] 이 세 값에 의해서만 영향을 받기 때문)
	 * 
	 * --- DP 아이디어 잘 떠올리는 법 ---
	 * 1. 부분 문제, 중복되는 문제를 찾기
	 * 2. 상태를 정의하기, 즉 어떤 정보까지 알아야 문제를 부분 문제로 쪼갤 수 있는지 살피기
	 * 3. 점화식(상태 전이) 찾기
	 * 4. 초기 조건 설정
	 * 
	 */
}
