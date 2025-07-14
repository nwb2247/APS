import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		boolean[] arr = new boolean[21];
		
		int N = Integer.parseInt(br.readLine());
		for (int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			String op = st.nextToken();
			int x = 0;
			switch (op) {
			case "add" :
				x = Integer.parseInt(st.nextToken());
				arr[x] = true;
				break;
			case "remove" :
				x = Integer.parseInt(st.nextToken());
				arr[x] = false;
				break;
			case "check" :
				x = Integer.parseInt(st.nextToken());
				if (arr[x]) {
					sb.append("1");
				} else {
					sb.append("0");
				}
				sb.append("\n");
				break;
			case "toggle" :
				x = Integer.parseInt(st.nextToken());
				arr[x] = !arr[x];
				break;
			case "all" :
				Arrays.fill(arr, true);
				break;
			case "empty" :
				Arrays.fill(arr, false);
			}
		}
		System.out.println(sb.toString());
		
	}
    
}