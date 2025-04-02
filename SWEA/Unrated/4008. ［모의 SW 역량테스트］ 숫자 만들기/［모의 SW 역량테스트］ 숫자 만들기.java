import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	
	static int N;
	static int[] operator;
	static int[] number;
	static int[] permuted;
	
	static int max, min;
 
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		
		for (int t=1; t<=T; t++) {
			
			// 입력을 받는 부분
			N = Integer.parseInt(br.readLine());
			
			operator = new int[4];
			st = new StringTokenizer(br.readLine());
			// 0:+ 1:- 2:* 3:/
			for (int i=0; i<4; i++) {
				operator[i] = Integer.parseInt(st.nextToken());
			}
			
			number = new int[N];
			st = new StringTokenizer(br.readLine());
			for (int i=0; i<N; i++) {
				number[i] = Integer.parseInt(st.nextToken());
			}
			
			// 순열위한 배열 생성, min, max 값 초기화
			permuted = new int[N-1];
			min = Integer.MAX_VALUE;
			max = Integer.MIN_VALUE;

			perm(0);
			sb.append("#").append(t).append(" ").append(max-min).append("\n");
			
		}
		
		System.out.println(sb);

	}
	
	private static void perm(int cnt) {
		
		if (cnt == N-1) {
			
			// 연산
			int val = number[0];
			for (int i=1; i<N; i++) {
				switch(permuted[i-1]) {
				case 0 :
					val += number[i];
					break;
				case 1 :
					val -= number[i];
					break;
				case 2 :
					val *= number[i];
					break;
				case 3: 
					val /= number[i];
					break;
				}
			}
			
			min = Math.min(min, val);
			max = Math.max(max, val);
			
			return;
		}
		
		// 연산자 순열을 생성, 단 동일한 순열이 완성되는 경우 하나의 순열로 간주
		// 이를 위해서 연산자 갯수 배열을 기준으로 순열 생성 
		for (int i=0; i<4; i++) {
			if (operator[i] == 0) continue; // 해당 연산자의 수가 남아있지 않다면 패스
			permuted[cnt] = i;				// 남아있다면 사용
			operator[i]--; 					// 각 연산자를 하나 사용할 때 마다 연산자 갯수를 -1
			perm(cnt+1);					// 재귀로 순열생성
			operator[i]++;					// 포함한 순열에 대한 탐색 끝나면 다시 갯수를 늘려줌
		}
		
	}


}



