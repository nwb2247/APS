import java.io.BufferedReader;
import java.io.IOError;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		int max = 1000000;
		int div = 1000000009;
		int[][] arr = new int[max+1][4];
		
		// 두번째 차원의미 : 마지막으로 더해진 수
		arr[1][1] = 1; // 1
		arr[2][1] = 1; // 1+1
		arr[2][2] = 1; // 2
		arr[3][1] = 2; // 1+1+1 2+1
		arr[3][2] = 1; // 1+2
		arr[3][3] = 1; // 3
		
		for (int i=4; i<=max; i++) {
			for(int j=1; j<=3; j++) {
				for(int k=1; k<=3; k++) {
					arr[i][j] = (arr[i][j]%div + arr[i-j][k]%div)%div;
				}
			}
		}

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		for (int t=1; t<=T; t++) {
			int num = Integer.parseInt(br.readLine());
			int sol=0;
			for (int i=1; i<=3; i++) {
				sol = (sol%div + arr[num][i]%div)%div;
			}
			sb.append(sol + "\n");
		}
		
		System.out.println(sb);
		
	}
	
}
