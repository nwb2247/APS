import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
	
	static int cardNum = 9;

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		
		for (int t=1; t<=T; t++) {
			
			// 상대 카드와 내 카드 초기화
			int[] oppo = new int[cardNum];
			int[] my = new int[cardNum];
			boolean[] oppoBool = new boolean[2*cardNum+1];
			
			st = new StringTokenizer(br.readLine());
			for (int i=0; i<cardNum; i++) {
				oppo[i] = Integer.parseInt(st.nextToken());
				oppoBool[oppo[i]] = true;
			}
			
			int j=1; // 1번부터 상대카드인지 확인
			for (int i=0; i<cardNum; i++) {
				while(oppoBool[j]) {
					j++;
				}
				my[i] = j++;
			}
			
			int[] output = new int[cardNum];
			boolean[] visited = new boolean[cardNum];
			
//			System.out.println(Arrays.toString(oppo));
//			System.out.println(Arrays.toString(my));
			
			int[] gameCnt = new int[2]; // 0: 패배 1: 승리
			
			permute(my, 0, visited, output, oppo, gameCnt);
			
			System.out.println("#" + t + " " + gameCnt[0] + " " + gameCnt[1]);

			
			
		}

	}
	
	public static void permute(int[] my, int depth, boolean[] visited, int[] output, int[] oppo, int[] gameCnt) {
		
		if (depth == output.length) {
			int myPoint = 0;
			int oppoPoint = 0;
			for (int i=0; i<cardNum; i++) {
				if (output[i] < oppo[i]) {
					oppoPoint += output[i] + oppo[i];
				} else {
					myPoint += output[i] + oppo[i];
				}
			}
			
			if (oppoPoint > myPoint) {
				gameCnt[0]++;
			} else {
				gameCnt[1]++;
			}
			
			return;
		}
		
		// 수열 생성
		for (int i=0; i<cardNum; i++) {
			if (!visited[i]) {
				
				// output에 넣음
				output[depth] = my[i];
				visited[i] = true;
				
				// 나머지 돌림
				permute(my, depth+1, visited, output, oppo, gameCnt);
				
				// 넣었던 것 다시 뺌
				visited[i] = false;
			}
		}
		
		
	}

}
