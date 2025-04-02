import java.io.*;
import java.util.*;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		 for (int t=1; t<=10; t++) {
			 int N = Integer.parseInt(br.readLine());
			 
			 int[] buildings = new int[N];
			 
			 StringTokenizer st = new StringTokenizer(br.readLine());
			 
			 for(int i=0; i<N; i++) {
				 buildings[i] = Integer.parseInt(st.nextToken());
				 
			 }
			 
			 int count=0;
			 int K = 2;
			 for (int i=0; i<N; i++) {
				 int start = Math.max(0, i-K);
				 int end = Math.min(N-1, i+K);
				 
				 int view = Integer.MAX_VALUE;
				 for(int j=start; j<=end; j++) {
					 
					 if (i == j) {
						 continue;
					 } // 본인 과의 차이는 0이므로 구하지 않음
					 
					 int new_v = buildings[i] - buildings[j];
					 if (new_v <= 0) {
						 view = 0;
						 break;
					 }
					 view = Math.min(view, new_v);
				 }
				 count += view;
			 }
			 
			 System.out.println("#"+t+" "+count);
			 
		 }
	}
}