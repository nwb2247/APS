import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		int[] mMax = new int[N*100+1]; // mMax[cost] 해당 cost소모시 확보가능한 최대 메모리 크기
		
		int[] mSize = new int[N];
		int[] cost = new int[N];
		
		st = new StringTokenizer(br.readLine());
		for (int i=0; i<N; i++) {
			mSize[i] = Integer.parseInt(st.nextToken());
		}
		
		st = new StringTokenizer(br.readLine());
		for (int i=0; i<N; i++) {
			cost[i] = Integer.parseInt(st.nextToken());
		}
		
		for (int i=0; i<N; i++) {
			for (int c=N*100; c>= cost[i]; c--) {
				mMax[c] = Math.max(mMax[c], mMax[c-cost[i]]+mSize[i]);
			}
		}
		
		
//		System.out.println(Arrays.toString(mMax));
		
		for (int c=0; c<=N*100; c++) {
			if (mMax[c] < M) continue;
			System.out.println(c);
			break;
		}
		
		
		
	}

}
