// BJ10824 네 수 

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		String StrA = st.nextToken();
		String StrB = st.nextToken();
		String StrC = st.nextToken();
		String StrD = st.nextToken();
		
		long A = Integer.parseInt(StrA);	// 범위가 1000000까지 이고 이 둘을 이어붙여야하므로 BigInteger를 사용해야함. 이를 위해서 long으로 입력을 받아야 함
		long B = Integer.parseInt(StrB);	
		long C = Integer.parseInt(StrC);	
		long D = Integer.parseInt(StrD);
		
		
		BigInteger AB = BigInteger.valueOf(A).multiply(BigInteger.TEN.pow(StrB.length())).add(BigInteger.valueOf(B)); // StrB 길이 만큼 10을 제곱해서 AB를 붙이는 효과
		BigInteger CD = BigInteger.valueOf(C).multiply(BigInteger.TEN.pow(StrD.length())).add(BigInteger.valueOf(D));
		
		System.out.println(AB.add(CD));
		
		
		
	}

}
