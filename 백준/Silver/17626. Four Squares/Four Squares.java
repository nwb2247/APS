import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		
		int[] DP = new int[N+1];
		for (int i=1; i<=N; i++) {
			DP[i] = i;
			int maxSq = (int) Math.sqrt(i);
			for (int j=1; j<=maxSq; j++) {
				DP[i] = Math.min(DP[i], DP[i-j*j]+1);
			}
		}
		System.out.println(DP[N]);
		
	}
    
}

/*
 	- 접근 방법 DP
 	배열을 DP[i] = i 로 초기화하고 (가장 작은 제곱수 1+1+1+...을 i번)
 	각 i마다 1,4,9..., j*j (i보다 작은 제곱수 중 최대값)을 돌면서
 	DP[i] = Math.min(DP[i], DP[i-j*j]+1); 를 구함
 	ex) N = 12
 	12, 
 	DP[12-1]+1 = DP[11]+1
 	DP[12-4]+1 = DP[9]+1
 	DP[12-9]+1 = DP[3]+1
 	중 가장 작은 값
 	
 	--------------------------------------------------------
 	
 	- 첫번째 시도 (비효율 DP, 시간 초과)
 	for (int i=2; i<=N; i++) {
		if (DP[i] == 1) continue;
		DP[i] = 4;
		for (DP j=0; j<=(i-1)/2; j++) {
			DP[i] = Math.min(DP[i], DP[1+j] + DP[i-1-j]);
			if (DP[i] == 2) break;
		}
	}
	
	DP[i]를 DP[1+j] + DP[i-1-j]의 합으로 구함
	O(N)의 루프를 두번 도므로 O(N^2)
	
	- 두번째 시도 (브루트 포스)
	1,2,3인경우를 각각 고려하여 여러번 루프를 돎
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
	
 * 
 * 
 * 
 * 
 */

