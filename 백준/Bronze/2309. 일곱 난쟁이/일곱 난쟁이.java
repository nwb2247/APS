import java.io.*;
import java.util.*;

class Main {

	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
		
		ArrayList<Integer> nums = new ArrayList<>();
		
		int sum = 0;
		for (int i=0; i<9; i++) {
			nums.add(Integer.parseInt(br.readLine()));
			sum += nums.get(i);
		}
		
		int i=0;
		int j=1;
		
		outer:
		for (i=0; i<9-1; i++) {
			for (j=i+1; j<9; j++) {
				if (sum - (nums.get(i) + nums.get(j)) == 100) {
					break outer;
				}
			}
		}
		
		nums.remove(j);
		nums.remove(i);
		nums.sort(Comparator.naturalOrder());
		
		for (int k=0; k<7; k++) {
			System.out.println(nums.get(k));
		}
		
		
	}

}