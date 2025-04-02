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
		
		int T = Integer.parseInt(br.readLine());
		
		for (int t=1; t<=T; t++) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int L = Integer.parseInt(st.nextToken());
			int[] score = new int[N];
			int[] cal = new int[N];
			
			int max = 0;
			
			for (int i=0; i<N; i++) {
				st = new StringTokenizer(br.readLine());
				score[i] = Integer.parseInt(st.nextToken());
				cal[i] = Integer.parseInt(st.nextToken());
			}
			
			for (int i=0; i<=N; i++) {
				int[] bitmask = new int[N];
				for (int j=0; j<i; j++) {
					bitmask[N-1-j] = 1; 
				}
				
				do {
//					System.out.println(Arrays.toString(bitmask));
					int sumScore = 0;
					int sumCal = 0;
					for (int k=0; k<N; k++) {
						if (bitmask[k] == 1) {
							sumScore += score[k];
							sumCal += cal[k];
						}
					}
					
					if (sumCal <= L) {
						max = Math.max(max, sumScore);
					}
					
					
				} while (combByNextPerm(bitmask));
				
			}
			
			sb.append("#" + t + " " + max + "\n");
			
		}
		
		System.out.println(sb);
		
		

	}
	
	private static boolean combByNextPerm(int[] bitmask) {
		
		// 1. 맨 뒤부터 탐색하여 bitmask[i-1] < bitmask[i]을 만족하는 최초의 i를 찾기
		int i = bitmask.length-1;
		while (i>0 && bitmask[i-1]>=bitmask[i]) {
			i--;
		}
		
		if (i<=0) return false; // 전체가 내림차순이면 마지막 순열이므로 종료
		
		// 2. comb[i-1]보다 큰 값중에서 가장 작은 값
		// (즉, 뒤쪽부터 탐색하여 처음 만나는 값)을 찾음.
		int j = bitmask.length-1;
		while (bitmask[j] <= bitmask[i-1]) {
			j--;
		}
		
		// 3. comb[i-1]과 comb[j]의 값을 swap
		int temp = bitmask[i-1];
		bitmask[i-1] = bitmask[j];
		bitmask[j] = temp;
		
		// 4. i번째 위치부터 끝까지 오름차순 정렬
		// (즉, 역순으로 되어있으므로 뒤집어 오름차순으로 만듦)
		j = bitmask.length-1;
		while (i<j) {
			temp = bitmask[i];
			bitmask[i] = bitmask[j];
			bitmask[j] = temp;
			i++;
			j--;
		}
		
		return true;
		
	}

}
