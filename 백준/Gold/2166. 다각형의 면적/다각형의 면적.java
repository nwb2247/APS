import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		
		long[][] p = new long[N][2];
		
		long minX = 100001;
		long minY = 100001;
		int start = -1;
		
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			p[i][0] = Integer.parseInt(st.nextToken());
			p[i][1] = Integer.parseInt(st.nextToken());
			if (p[i][0] < minX) {
				minX = p[i][0];
				start = i;
			}
			if (p[i][1] < minY) {
				minY = p[i][1];
			}
		}
		
		long size = 0;		

		for (int i=0; i<N; i++) {
			int prev = (start+i)%N;
			int cur = (prev+1)%N;
			long dX = p[cur][0]-p[prev][0]; // 양수면 면적 증가, 음수면 면적 감소
			size += dX * (p[cur][1]-minY + p[prev][1]-minY ); // 나누기 2는 맨 마지막에 진행
			prev = cur;
			cur = (cur+1)%N;
		}
		
		if (size%2 == 0) {
			System.out.println(Math.abs(size/2)+"."+"0");
		} else {
			System.out.println(Math.abs(size/2)+"."+"5");
		}
		
	}
	

}
