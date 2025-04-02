import java.util.*;
import java.io.*;

class Solution {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		String input = br.readLine();
		StringTokenizer st = new StringTokenizer(input, " ");
		
		int[] scores = new int[N];
		for(int i=0; i < N; i++) {
			scores[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(scores);
		
		// int/int 하면 몫이 나옴 (나머지는 % / 소수점 포함은 double로 형변환 후)
		System.out.println(scores[N/2]);

	}

}
