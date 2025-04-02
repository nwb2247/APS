import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int N;
	static int[][] mat;
	
	static int[] order;
	static boolean[] isSelected;
	static int max;

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N = Integer.parseInt(br.readLine());
		
		mat = new int[N][9];
		
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j=0; j<9; j++) {
				mat[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		order = new int[9];
		order[3] = 0;
		isSelected = new boolean[9];
		isSelected[0] = true;
		max = 0;
		perm(0);
		System.out.println(max);

	}
	
	private static void perm(int cnt) {
		
		if (cnt == 9) {
//			System.out.println(Arrays.toString(order));
			max = Math.max(max, score());
			return;
		} else if (cnt == 3){ // 1번 4번 타자는 고정
			perm(cnt+1);
			return;
		}
		
		for (int i=0; i<9; i++) {
			if (isSelected[i]) continue;
			order[cnt] = i;
			isSelected[i] = true;
			perm(cnt+1);
			isSelected[i] = false;
		}
		
	}
	
	private static int score() {
		
		int out = 0;
		int cnt = 0;
		boolean[] base = new boolean[5]; // 0이 홈베이스 (타자) 4는 주자가 들어올때 홈베이스
		
		int idx = 0;
		
		for (int inn=0; inn<N; inn++) {
			out = 0;
			while(out < 3) {
				if (mat[inn][order[idx]] == 0) {
					out++;
				} else { // 안타 이상
					base[0] = true;
					for (int h=1; h<=mat[inn][order[idx]]; h++) {
						for (int r=3; r>=0; r--) {
							base[r+1] = base[r];
						}
						if (base[4]) cnt++;
						base[0] = false;
					}
				}
				idx = (idx+1) % 9;
			}
			for (int b=0; b<5; b++) {
				base[b] = false;
			}
		}
		
		return cnt++;

	}
}