import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	
	//BJ10844 쉬운계단수
	public static void main(String[] args) throws Exception {
		
		int[] cnt = new int[10];
		for (int i=1; i<=9; i++) {
			cnt[i] = 1;
		}
		
		int div = 1000000000;
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		int[] newCnt;
		for (int i=2; i<=N; i++) {
			newCnt = new int[10];
			for (int j=0; j<=9; j++) {
				if (j-1 >= 0) {
					newCnt[j-1] = (newCnt[j-1]%div + cnt[j]%div)%div;
				}
				if (j+1 < 10) {
					newCnt[j+1] = (newCnt[j+1]%div + cnt[j]%div)%div;
				}
			}
			
			cnt = newCnt;
			
		}
		
		int sol=0;
		for (int i=0; i<=9; i++) {
			sol = (sol%div + cnt[i]%div)%div;
		}

		System.out.println(sol);
		
	}

}
