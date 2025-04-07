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
		
		
		
		int[] mSize = new int[N];
		int[] cost = new int[N];
		int costSum = 0;
		
		st = new StringTokenizer(br.readLine());
		for (int i=0; i<N; i++) {
			mSize[i] = Integer.parseInt(st.nextToken());
		}
		
		st = new StringTokenizer(br.readLine());
		for (int i=0; i<N; i++) {
			cost[i] = Integer.parseInt(st.nextToken());
			costSum += cost[i];
		}
		
		
		int[] mMax = new int[costSum+1]; // mMax[cost] 해당 cost소모시 확보가능한 최대 메모리 크기		
		for (int i=0; i<N; i++) {
			for (int c=costSum; c>= cost[i]; c--) {
				mMax[c] = Math.max(mMax[c], mMax[c-cost[i]]+mSize[i]);
			}
		}
		
//		System.out.println(Arrays.toString(mMax));
		
		int left = 0;
		int right = costSum;
		int sol = -1;
		
		while (left<=right) {
			int mid = (left+right)/2;
			if (mMax[mid] >= M) {
				sol = mid;
				right = mid-1;
			} else {
				left = mid+1;
			}
		}
		
		System.out.println(sol);
		
		
		
	}

}
