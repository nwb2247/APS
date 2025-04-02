import java.io.*;
import java.util.*;

class Main {

	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int MaxW = Integer.parseInt(st.nextToken());
		int MaxH = Integer.parseInt(st.nextToken());
		
		ArrayList<Integer> WList = new ArrayList<>();
		ArrayList<Integer> HList = new ArrayList<>();
		
		WList.add(0);
		HList.add(0);
		
		int N = Integer.parseInt(br.readLine());
		
		for(int n=0; n<N; n++) {
			st = new StringTokenizer(br.readLine());
			if(Integer.parseInt(st.nextToken()) == 0) {
				HList.add(Integer.parseInt(st.nextToken()));
			} else {
				WList.add(Integer.parseInt(st.nextToken()));
			}
		}
		
		WList.add(MaxW);
		HList.add(MaxH);
		
		WList.sort(Comparator.naturalOrder());
		HList.sort(Comparator.naturalOrder());		
		
		int Wlong = 0;
		for(int i=0; i<WList.size()-1; i++) {
			Wlong = Math.max(Wlong, WList.get(i+1) - WList.get(i));
		}
		
		int Hlong = 0;
		for(int i=0; i<HList.size()-1; i++) {
			Hlong = Math.max(Hlong, HList.get(i+1) - HList.get(i));
		}
		
		System.out.println(Wlong*Hlong);
		
	}
}
