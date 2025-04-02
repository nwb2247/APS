import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		StringBuilder sb = new StringBuilder();
		
		for (int t=1; t<=T; t++) {
			int testNum = Integer.parseInt(br.readLine());
			int[] cnt = new int[101];
			
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			int maxNum = 0;
			int max = 0;
			for (int i=0; i<1000; i++) {
				int num = Integer.parseInt(st.nextToken());
				cnt[num]++;
				if (cnt[num] > max || (cnt[num] == max && num > maxNum)) {
					maxNum = num;
					max = cnt[num];
				}
			}
			
			sb.append("#"+testNum+" "+maxNum+"\n");
			
		}
		System.out.println(sb);

	}

}
