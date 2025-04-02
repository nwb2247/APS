import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		int two = PrimePowerOfNumFactorial(N, 2) - PrimePowerOfNumFactorial(M, 2) - PrimePowerOfNumFactorial(N-M, 2);
		int five = PrimePowerOfNumFactorial(N, 5) - PrimePowerOfNumFactorial(M, 5) - PrimePowerOfNumFactorial(N-M, 5);
		
		System.out.println(Math.min(two, five));
		

		
	}
	
	// num! (num의 팩토리얼)소인수 분해시 소수 prime이 몇승인지 찾는 방법
	public static int PrimePowerOfNumFactorial(int num, int prime) {
		int count = 0;
		int CopyNum = num;
		while (CopyNum>1) {
			count += CopyNum/prime; // prime으로 나눴을 때의 몫을 더해준다.
			CopyNum = CopyNum/prime; //
		}
		return count;
	}
	/*
	 * ex) 20 , 2
	 * 
	 * loop1; 
	 * count += CopyNum/prime : 20 / 2 -> 10 (2 4 6 8 10 13 14 16 18 20) 2^1를 갖는 수 10개
	 * loop2;
	 * count += CopyNum/prime : 10 / 2 -> 5 (4 8 12 16 20) 2^2를 갖는 수 5개
	 * loop3;
	 * count += CopyNum/prime : 5 / 2 -> 2 (8 16) 2^3를 갖는 수 2개
	 * loop4;
	 * count += CopyNum/prime : 2 / 1 -> 1 (16) 2^4를 갖는 수 1개
	 * 즉 20!은 10+5+2+1 = 18 => 2^18을 소인수로 갖는다.
	 */

}
