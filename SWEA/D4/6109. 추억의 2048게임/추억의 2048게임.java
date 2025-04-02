import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		
		for (int t=1; t<=T; t++) {
			
			st = new StringTokenizer(br.readLine());
			
			int N = Integer.parseInt(st.nextToken());
			String dir = st.nextToken();
		 	
			int[][] map = new int[N][N];
			for (int r=0; r<N; r++) {
				st = new StringTokenizer(br.readLine());
				for (int c=0; c<N; c++) {
					map[r][c] = Integer.parseInt(st.nextToken());
				}
			}
			
			if (dir.equals("up")) {
				for (int c=0; c<N; c++) {
					int cur = 0; // 현재 완성 시켜야하는 인덱스 
					for (int r=1; r<=N-1; r++) {
						if (map[r][c] == 0) continue;
						if (map[cur][c] != 0) { 			// [cur][c]이 0이 아니라면
							if (map[r][c] == map[cur][c]) {	// [cur][c]이 0이 아니고 [r][c]과 같을 때
								map[cur++][c] *= 2;			// [cur][c]을 2배로 하고 cur++
								map[r][c] = 0;
							} else { 						// [cur][c]이 0이 아니고 [r][c]과 다를 때
								map[++cur][c] = map[r][c];	// 미리 cur을 1더하고 다른 값을 입력
								if (cur == r) continue;		// cur == r 이면 지우지 말아야하는 걸 지우게 되므로 넘어감
								map[r][c] = 0;				
							}
						} else { // map[cur][c] == 0;
							map[cur][c] = map[r][c];
							map[r][c] = 0;
						}
					}	
				}
				
			} else if (dir.equals("down")) {
				for (int c=0; c<N; c++) {
					int cur = N-1;
					for (int r=N-2; r>=0; r--) {
						if (map[r][c] == 0) continue;
						if (map[cur][c] != 0) { 			
							if (map[r][c] == map[cur][c]) {	
								map[cur--][c] *= 2;			
								map[r][c] = 0;
							} else { 						
								map[--cur][c] = map[r][c];	
								if (cur == r) continue;		
								map[r][c] = 0;				
							}
						} else {
							map[cur][c] = map[r][c];
							map[r][c] = 0;
						}
					}		
				}
				
			} else if (dir.equals("left")) {
				for (int r=0; r<N; r++) {
					int cur = 0;
					for (int c=1; c<=N-1; c++) {
						if (map[r][c] == 0) continue;
						if (map[r][cur] != 0) { 			
							if (map[r][c] == map[r][cur]) {
								map[r][cur++] *= 2;			
								map[r][c] = 0;
							} else { 					
								map[r][++cur] = map[r][c];	
								if (cur == c) continue;		
								map[r][c] = 0;				
							}
						} else { // map[last][c] == 0;
							map[r][cur] = map[r][c];
							map[r][c] = 0;
						}
					}	
				}
				
			} else { // dir.equals("right")
				for (int r=0; r<N; r++) {
					int cur = N-1;
					for (int c=N-2; c>=0; c--) {
						if (map[r][c] == 0) continue;
						if (map[r][cur] != 0) { 			
							if (map[r][c] == map[r][cur]) {
								map[r][cur--] *= 2;			
								map[r][c] = 0;
							} else { 					
								map[r][--cur] = map[r][c];	
								if (cur == c) continue;		
								map[r][c] = 0;				
							}
						} else {
							map[r][cur] = map[r][c];
							map[r][c] = 0;
						}
					}	
				}
				
			}
			
			sb.append("#")
			.append(t)
			.append("\n");
			
			for (int r=0; r<N; r++) {
				for (int c=0; c<N; c++) {
					sb.append(map[r][c]+" ");
				}
				sb.append("\n");
			}
			
		}
		
		System.out.println(sb);
		

	}

}
