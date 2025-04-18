import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int TC = Integer.parseInt(br.readLine());
		
		for (int tc=1; tc<=TC; tc++) {
			int N = Integer.parseInt(br.readLine());
			int cnt = 0;
			int digitCnt = 0;
			boolean[] check = new boolean[10];
			
			int num = N;
			while(true) {
				
//				System.out.println("num : " + num);
//				System.out.println(Arrays.toString(check));
				
				int cur = num;
				while (cur != 0) {
					if(!check[cur%10]) {
						check[cur%10] = true;
						digitCnt++;
					}
					cur /= 10;
				}
				
				if (digitCnt == 10) {
					break;
				}
				num = (++cnt)*N;
				
			}
			
			sb.append("#").append(tc).append(" ").append(num).append("\n");

		}
		
		System.out.println(sb.toString());

	}

}
