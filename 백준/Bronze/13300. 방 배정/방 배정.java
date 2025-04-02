import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		int[][] roomCnt = new int[2][7]; // 1~6 학년 0:여 1:남
		int[][] memCnt = new int[2][7];
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int g = Integer.parseInt(st.nextToken());
			
			memCnt[s][g]++;
			if (memCnt[s][g] == K) {
				memCnt[s][g] = 0;
				roomCnt[s][g]++;
			}
		}
		
		int sol = 0;
		for (int s=0; s<=1; s++) {
			for (int g=1; g<=6; g++) {
				if (memCnt[s][g] != 0) {
					roomCnt[s][g]++;
				}
				
				sol += roomCnt[s][g];
			}
		}
		
		System.out.println(sol);
 		

	}

}
