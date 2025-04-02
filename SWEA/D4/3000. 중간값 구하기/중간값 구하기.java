import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Solution {
	// SWEA3000
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		int mod = 20171109;
		
		for (int t=1; t<=T; t++) {
			
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			int N = Integer.parseInt(st.nextToken());
			int mid = Integer.parseInt(st.nextToken());
			
			PriorityQueue<Integer> minHeap = new PriorityQueue<>();
			PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
			
			int sum = 0;
			for (int i=0; i<N; i++) {
				
				st = new StringTokenizer(br.readLine());
				while(st.hasMoreTokens()) {
					int e = Integer.parseInt(st.nextToken());
					if (e > mid) {
						minHeap.add(e);
					} else {
						maxHeap.add(e);
					}
				}
				
				while(minHeap.size() != maxHeap.size()) {
					if (minHeap.size() > maxHeap.size()) {
						maxHeap.add(mid);
						mid = minHeap.poll();
					} else {
						minHeap.add(mid);
						mid = maxHeap.poll();
					}
				}
				
				sum = (sum + mid%mod)%mod;
				
				
			}
			
			System.out.println("#" + t + " " + sum);

			
		}
		
	}
}

