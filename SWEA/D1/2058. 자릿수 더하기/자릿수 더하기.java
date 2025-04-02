import java.io.*;
import java.util.*;

class Solution {
	public static void main(String [] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		
		int sum = 0;
		for(int i=0; i < input.length(); i++) {
			sum += Integer.parseInt(String.valueOf(input.charAt(i)));
		}
		
		System.out.println(sum);
	}
}