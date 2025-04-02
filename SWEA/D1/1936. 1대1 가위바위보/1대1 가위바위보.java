import java.io.*;
import java.util.*;

class Solution {
	public static void main(String [] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		StringTokenizer st = new StringTokenizer(input, " ");
		int A = Integer.parseInt(st.nextToken());
		int B = Integer.parseInt(st.nextToken());
		
		String winner;
		if(A == 1) {
			if (B == 2) winner = "B"; else winner = "A";
		} else if(A == 2) {
			if (B == 3) winner = "B"; else winner = "A";
		} else { // A == 3
			if (B == 1) winner = "B"; else winner = "A";
		}
		
		System.out.println(winner);
	}
}