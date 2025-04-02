// BJ 11655 ROT13

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {
		 // TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int A = (int) 'A';
		int Z = (int) 'Z';
		int a = (int) 'a';
		int z = (int) 'z';
		
		char[] chars = br.readLine().toCharArray();
		
		StringBuilder sb = new StringBuilder();
		for (char c : chars) {
			int cInt = (int) c;
			
			if (c>= a && c<= z) {
				char cNew = (char) ((cInt - a + 13) % 26 + a);
				sb.append(cNew);
			} else if (c>= A && c<= Z) {
				char cNew = (char) ((cInt - A + 13) % 26 + A);
				sb.append(cNew);
			} else {
				sb.append(c);
			}
		}
		
		System.out.println(sb);	

	}

}
