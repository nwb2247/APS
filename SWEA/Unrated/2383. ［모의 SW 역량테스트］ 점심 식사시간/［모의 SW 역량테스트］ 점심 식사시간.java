import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Solution {
	
	static int N;
	static ArrayList<int[]> pList;
	static ArrayList<int[]> sList;
	static ArrayList<ArrayList<Integer>> aList; // 도착시간
	static int sol;

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		
		for (int t=1; t<=T; t++) {
			
			pList = new ArrayList<>();
			sList = new ArrayList<>();
			aList = new ArrayList<>();
			for (int i=0; i<2; i++) {
				aList.add(new ArrayList<>());
			}
			
			N = Integer.parseInt(br.readLine());
			
			for (int r=0; r<N; r++) {
				st = new StringTokenizer(br.readLine());
				for (int c=0; c<N; c++) {
					int val = Integer.parseInt(st.nextToken());
					if (val == 0) {
						continue;
					} else if (val == 1) {
						pList.add(new int[] {r,c});
					} else {
						sList.add(new int[] {r,c,val});
					}
				}
			}
//			for (int[] s : sList) {
//				System.out.println(Arrays.toString(s));
//			}
			
			sol = Integer.MAX_VALUE;
			subset(0);
			
			sb.append("#").append(t).append(" ").append(sol).append("\n");
			
		}
		
		System.out.println(sb.toString());
		

	}
	
	private static int calDist(int[] p, int[] c) {
		return Math.abs(p[0]-c[0]) + Math.abs(p[1]-c[1]);
	}
	
	private static void subset(int idx) {
		if (idx == pList.size()) {
			solve();
			
			return;
		}
		
		for (int i=0; i<2; i++) {
			aList.get(i).add(calDist(pList.get(idx), sList.get(i)));
			subset(idx+1);
			aList.get(i).remove(aList.get(i).size()-1); // removeLast
		}
		
	}
	
	private static void solve() {
		
		int max = 0;
	
		
		for (int i=0; i<2; i++) {
			
			if (aList.get(i).isEmpty()) continue;
			
			int slen = sList.get(i)[2];
			
			ArrayList<Integer> dList = new ArrayList<>();
			for (int t : aList.get(i)) {
				dList.add(t + 1); // 도착 1분후 출발하므로 +1
			}
			dList.sort(Comparator.naturalOrder());
			
//			if (dList.size() <= 3) {
//				
//			}
			
			for (int j=3; j<dList.size(); j++) {
				dList.set(j, Math.max(dList.get(j), dList.get(j-3) + slen));
			}
			
			max = Math.max(max, dList.get(dList.size()-1) + slen); // 출발시간 + 계단길이 
			// getLast
			
		}
		
		sol = Math.min(sol, max);
	}

}



























