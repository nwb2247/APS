import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		
		int sol = 4;
		int end = (int) Math.sqrt(N);
		
		boolean found = false;
		for (int i=1; i<=end; i++) {
			if (i*i == N) {
				sol = 1;
				found = true;
				break;
			}
		}
		if (!found) {
			outer : 
			for (int i=1; i<=end; i++) {
				if (2*i*i == N) {
					sol = 2;
					found = true;
					break outer;
				}
				for (int j=0; j<=end; j++) {
					if (j*j + i*i == N) {
						sol = 2;
						found = true;
						break outer;
					}
				}
			}
		}
			
		if (!found) {
			outer : 
			for (int i=1; i<=end; i++) {
				// 3
				if (3*i*i == N) {
					sol = 3;
					break outer;
				}
				for (int j=0; j<=end; j++) {
					if (j*j + 2*i*i == N) {
						sol = 3;
						break outer;
					}
					for (int k=0; k<=end; k++) {
						if (i*i + j*j + k*k == N) {
							sol = 3;
							break outer;
						}
					}
				}
			}
		}
		
		System.out.println(sol);
		
	}
    
}