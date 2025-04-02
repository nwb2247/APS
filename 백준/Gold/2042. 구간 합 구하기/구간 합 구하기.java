import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int N, M, K;
	static long[] arr;
	
	static long[] tree; 

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		arr = new long[N+1];
		
		for (int i=1; i<=N; i++) {
			arr[i] = Long.parseLong(br.readLine());
		}
		
		int height = (int) Math.ceil(Math.log(N)/Math.log(2));
		tree = new long[(int) Math.pow(2, height+1)];
		// height가 3이면 트리에는 2^3 + 2^2 + 2^1 + 2^0 = 2^4 - 1개 원소 갯수 필요
		// 그런데 1을 root로 만들어야 하므로 +1 해줘야 함 => 2^4 => 2^(h+1)
		
		// 초기화
		for (int i=1; i<=N; i++) {
			update(i, arr[i], 1, 1, N);
		}
		
		for (int i=0; i<M+K; i++) {
			st = new StringTokenizer(br.readLine());
			int op = Integer.parseInt(st.nextToken());
			
			if (op == 1) {
				int f = Integer.parseInt(st.nextToken());
				long s = Long.parseLong(st.nextToken());
				update(f, s-arr[f], 1, 1, N);
				arr[f] = s;
			} else {
				int f = Integer.parseInt(st.nextToken());
				int s = Integer.parseInt(st.nextToken());
				sb.append(sum(f, s, 1, 1, N)+"\n");
			}
		}
		
		System.out.println(sb);
		
	}
	
	public static void update(int i, long diff, int node, int left, int right) {
		// i : arr내 index, diff : 기존 값과의 차이
		// node : tree내 값을 변경할 인덱스
		// left, end : node에 해당하는 범위
		
		if (i < left || i > right) return;
		
		tree[node] += diff;
		
		if (left != right) {
			update(i, diff, node*2, left, (left+right)/2);
			update(i, diff, node*2+1, (left+right)/2+1, right);
		}
		
	}
	
	public static long sum(int start, int end, int node, int left, int right) {
		// start, end : 합을 구하고자 하는 구간
		// node : tree내 값을 변경할 인덱스
		// left, end : node에 해당하는 범위
		
		if (end < left || right < start) {
			return 0;
		} 
		
		if (start <= left && right <= end) {
			return tree[node];
		}
		
		return sum(start, end, node*2, left, (left+right)/2) +
				sum(start, end, node*2+1, (left+right)/2+1, right);
		
		
	}
	

}
