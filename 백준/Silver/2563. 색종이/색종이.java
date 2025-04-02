import java.io.*;
import java.util.*;

class Main {

	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
		
		ArrayList<ArrayList<Integer>> nums = new ArrayList<>(100);
		
		for(int i=0; i<100; i++) {
			nums.add(new ArrayList<>(100));
			for(int j=0; j<100; j++) {
				nums.get(i).add(0);
			}
		}
		
		int N = Integer.parseInt(br.readLine());
		
		for(int n=0; n<N; n++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int X = Integer.parseInt(st.nextToken());
			int Y = Integer.parseInt(st.nextToken());
			
			for(int x=X; x<X+10; x++) {
				for(int y=Y; y<Y+10; y++) {
					int origin = nums.get(y).get(x);
					nums.get(y).set(x, origin+1);
				}
			}	
			
		}
		
		int sum = 0;
		for(int i=0; i<100; i++) {
			for(int j=0; j<100; j++) {
				if (nums.get(i).get(j) > 0) sum++;
			}
		}
		
		System.out.println(sum);
	}
}
