import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Solution {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		for (int i=0; i<10; i++) {
			int t = Integer.parseInt(br.readLine());
			String patterStr = br.readLine();
			String textStr = br.readLine();
			
			System.out.println("#"+t+" "+BoyerMoore(textStr, patterStr));
			
			
		}
		
		
	}
	
	
	public static int BoyerMoore (String textStr, String patternStr) { // KMP에 비해 평균적으로 좋지만(O(N/M)) 최악의 경우 O(NM)
		
		char[] text = textStr.toCharArray();
		char[] pattern = patternStr.toCharArray();
		
		int N = text.length;
		int M = pattern.length;
		
		int i=0; 		// 텍스트 내 위치
		int j; 			// 패턴 내 위치
		
		int[] LOF = new int[(int) Math.pow(2,16)]; // Last Occurence Function
		// ASCII : 2^8 (알파벳 숫자)
		// 유니코드(UTF-16) 은 2^16 (한글, 이모지 등 포함)
		Arrays.fill(LOF, -1);
		for (int k=0; k<M; k++) {
			LOF[pattern[k]] = k;
		}

		int cnt = 0;
		
		while (i<=N-M) {
			
			for (j=M-1; j>=0; j--) { // 맨 뒤부터 일치하는지 확인
				
				if (text[i+j] == pattern[j]) {
					continue;
				} else {
					int l = LOF[text[i+j]];
					if (l == -1) {
						i = i+j+1;
					} else {
						if (l < j) {
							i=i+j-l;
						} else {
							i=i+1;
						}
					}
					break;
				}
			}
			
			if (j == -1) {
				cnt++; // j == -1, 즉 패턴을 모두 돌아도 다른 것이 없어 일치하는 것을 찾은 경우 
				i = i+1;
			}	

		}

		return cnt++;
		
	}

}
