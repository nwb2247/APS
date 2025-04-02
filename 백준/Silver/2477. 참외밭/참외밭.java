import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int K = Integer.parseInt(br.readLine());
		
		int[] dir = new int[6];
		int[] len = new int[6];
		
		int[] border = new int[4+1]; // 1:동 2:서 3:남 4:북
		int x = 0;
		int y = 0;
		
		for (int i=0; i<6; i++) {
			
			st = new StringTokenizer(br.readLine());
			dir[i] = Integer.parseInt(st.nextToken());
			len[i] = Integer.parseInt(st.nextToken());
			
			switch (dir[i]) {
			case 1 :
				x += len[i];
				border[dir[i]] = Math.max(border[dir[i]], x);
				break;
			case 2 :
				x -= len[i];
				border[dir[i]] = Math.min(border[dir[i]], x);
				break;
			case 3 :
				y -= len[i];
				border[dir[i]] = Math.min(border[dir[i]], y);
				break;
			case 4 :
				y += len[i];
				border[dir[i]] = Math.max(border[dir[i]], y);
				break;
			}
			
		}
		
		int width = Math.max(border[1]-border[2], border[2]-border[1]);
		int height = Math.max(border[3]-border[4], border[4]-border[3]);
		
		int area = width*height;
		
		for (int i=0; i<6; i++) {
			
			if (x != border[1] && x != border[2] && y != border[3] && y != border[4]) {
				area -= len[i] * len[(i+5)%6];
				break;
			}
			
			switch (dir[i]) {
			case 1 :
				x += len[i];
				break;
			case 2 :
				x -= len[i];
				break;
			case 3 :
				y -= len[i];
				break;
			case 4 :
				y += len[i];
				break;
			}
		}
		
		System.out.println(area*K);
		
	}
}
