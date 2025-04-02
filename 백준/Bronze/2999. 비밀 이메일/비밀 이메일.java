import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		char[] arr = br.readLine().toCharArray();
		
		int N = arr.length;
		int R = (int) Math.sqrt(N); // double을 int로 명시적 형변환 시, 내림의 결과를 반환
		int C = N/R;
		while(N%R != 0) {
			R--;
			C = N/R;
		}
		
//		System.out.println(R+" "+C);
		
		// "복호화" 이므로 정인이의 암호화 과정을 역으로 수행해야함
		char[][] matrix = new char[R][C];
		int idx = 0;
		
		for (int c=0; c<C; c++) { // 열 방향 순회
			for (int r=0; r<R; r++) {
				matrix[r][c] = arr[idx];
				idx++;
			}
		}
		
		StringBuilder sb = new StringBuilder();
		for(int r=0; r<R; r++) {
			for (int c=0; c<C; c++) {
				sb.append(matrix[r][c]);
			}
		}
		
		System.out.println(sb);
		

	}

}
