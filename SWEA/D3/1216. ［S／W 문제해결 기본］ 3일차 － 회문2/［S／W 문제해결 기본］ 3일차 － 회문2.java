import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Solution {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		for (int i=0; i<10; i++) {
			int t = Integer.parseInt(br.readLine());
			
			char[][] map = new char[100][];

			for (int j=0; j<100; j++) {
				map[j] = br.readLine().toCharArray();
			}

			
			int sol = 0;
			for (int r=0; r<100; r++) {
				for (int c=0; c<100; c++) {
					int oddLen = 1;
					int evenLen = 0;
					for (int d=1; d<=50; d++) {
						if (c-d>=0 && c+d<100 && map[r][c-d] == map[r][c+d]) {
							oddLen += 2;
						} else {
							break;
						}
					}
					
					for (int d=0; d<=50; d++) {
						if (c-d>=0 && c+d+1<100 && map[r][c-d] == map[r][c+d+1]) {
							evenLen += 2;
						} else {
							break;
						}
					}
					sol = Math.max(sol, Math.max(oddLen, evenLen));
					
				}
				
			}
			
			for (int c=0; c<100; c++) {
				for (int r=0; r<100; r++) {
					int oddLen = 1;
					int evenLen = 0;
					for (int d=1; d<=50; d++) {
						if (r-d>=0 && r+d<100 && map[r-d][c] == map[r+d][c]) {
							oddLen += 2;
						} else {
							break;
						}
					}
					
					for (int d=0; d<=50; d++) {
						if (r-d>=0 && r+d+1<100 && map[r-d][c] == map[r+d+1][c]) {
							evenLen += 2;
						} else {
							break;
						}
					}
					sol = Math.max(sol, Math.max(oddLen, evenLen));
					
				}
				
			}
			
			System.out.println("#"+t+" "+sol);

		}

	}

}
