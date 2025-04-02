import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int N, M, C, H;
	static ArrayList<int[]> chickenList, homeList;
	static int[] comb;
	
	static int sol;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		chickenList = new ArrayList<>();
		homeList = new ArrayList<>();

		for (int r=0; r<N; r++) {
			st = new StringTokenizer(br.readLine());
			for (int c=0; c<N; c++) {
				int val = Integer.parseInt(st.nextToken());
				if (val == 1) {
					homeList.add(new int[] {r,c});
				} else if (val == 2) {
					chickenList.add(new int[] {r,c});
				}
				
			}
			
		}
		
		C = chickenList.size();
		H = homeList.size();
		comb = new int[M];
		sol = Integer.MAX_VALUE;
		
		makeComb(0, 0);
		
		System.out.println(sol);

	}
	
	private static void makeComb(int start, int cnt) {
		
		if (cnt == M) {
//			System.out.println(Arrays.toString(comb));
			calDist();
			return;
		}
		
		for (int i=start; i<C; i++) {
			comb[cnt] = i;
			makeComb(i+1, cnt+1);
		}
 		
	}
	
	private static void calDist() {
		int sum = 0;
		for (int[] h : homeList) {
			int min = Integer.MAX_VALUE;
			for (int i=0; i<M; i++) {
				int[] c = chickenList.get(comb[i]);
				min = Math.min(min, Math.abs(h[0]-c[0]) + Math.abs(h[1]-c[1]));
			}
			sum += min;
			if (sum >= sol) return;
		}
		sol = Math.min(sol, sum);
	}

}
