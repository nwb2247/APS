import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
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
		
		// 메모리 범위가 1000000000이고 N이 최대 100이므로 최소 10억번의 연산이 발생하기 때문에
		// 각 메모리 사이즈에 대한 최소 비용으로 관리한다면 시간 초과 발생
		
		// 그러나 cost의 범위는 최대 100이므로 knapsack을 적용해볼만 함
		
		int[] mMax = new int[costSum+1]; // mMax[cost] 해당 cost소모시 확보가능한 최대 메모리 크기		
		for (int i=0; i<N; i++) {
			// 같은 앱이 두번 들어가지 않도록 하기 위해 역순으로 순회
			for (int c=costSum; c>= cost[i]; c--) {
				// mMax[c-cost[i]]+mSize[i] 즉, 현재 앱을 추가하는 것이 확보메모리가 더 크다면 갱신
				mMax[c] = Math.max(mMax[c], mMax[c-cost[i]]+mSize[i]);
			}
		}
		
//		System.out.println(Arrays.toString(mMax));
		// mMax는 자연스레 증가함수가 됨
		// 따라서 binary search로 M이상이 되는 최초의 비용을 구하면됨
		int left = 0;
		int right = costSum;
		int sol = -1;
		
		while (left<=right) {
			int mid = (left+right)/2;
			if (mMax[mid] >= M) { 	// M이상이 될때
				sol = mid;			// mid가 정답후보가 될 수 있으므로 저장해둠
				right = mid-1;
			} else {
				left = mid+1;
			}
		}
		
		// 출력
		System.out.println(sol);
		
		
		
	}

}
