import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int TC = Integer.parseInt(br.readLine());
		for (int tc=1; tc<=TC; tc++) {
			
			int N = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			
			int[] minLast = new int[N]; // minLast[len-1] : 증가부분수열의 길이가 len인 것중 마지막(가장큰)숫자가 가장 작은 것  
			int maxLen = 0;
			for (int i=0; i<N; i++) {
				int val = Integer.parseInt(st.nextToken());
				int pos = Arrays.binarySearch(minLast, 0, maxLen, val);
				/*
				 * 존재하면 해당인덱스, 
				 * 존재하지 않으면 -삽입될인덱스-1를 (0일 경우 -1을 반환하도록 하기 위해)
				 * 반환함
				 */
				
				int idx = -1; // 아무값이나 OK
				if (pos >= 0) {							// minLast에 중복으로 존재한다면 중복된 것 중 마지막인덱스 다음에 추가해야함
					for (int j=pos+1; j<N; j++) {
						if (minLast[j] == val) continue;
						idx = j;
						break;
					}
				} else {
					idx = (-pos)-1;						// minLast에 없다면 -pos-1에 삽입해야함
				}
				
				minLast[idx] = val;
				maxLen = Math.max(maxLen, idx+1);		// idx==len-1이므로 len=idx+1, 갱신 필요하다면 갱신
				
			}

			sb.append("#").append(tc).append(" ").append(maxLen).append("\n");			
			
		}
		
		System.out.println(sb.toString());

	}

}
