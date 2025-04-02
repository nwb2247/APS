import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {

	public static void main(String[] args) throws Exception {
		
//		for (int i=-10 ; i<=10; i ++) {
//			System.out.println(i + " 몫 " + i/(-2) + " 나머지 " + i%(-2));
//		} // 자바의 경우 음수/음수의 나머지는 음수로 계산됨 ex) -5 = -2*2 + (-1)
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		long N = Long.parseLong(br.readLine());
		
		StringBuilder sb = new StringBuilder();
		long Q = N;
		long R;
		while (true) {
			
			R = Q%(-2);
			Q = Q/(-2);
			
			if (R == -1) { // Q가 음수인경우 R이 0, -1가 나옴. 나머지가 0, 1이 되도록 조정해야함
				R += 2;
				Q += 1;
				 
			}
			
			sb.append(R);
			
			if (Q == 0) {
				System.out.println(sb.reverse());
				break;
			}				
		}
		
	}
	
// 2진수 , -2진수 계산하는 법 (2, -2 외에 다른 모든 수도 가능함)
	
//	13 2*6+1
//	6 2*3+0
//	3 2*1+1
//	1 2*0+1
//
//	=> 1*2^3 + 1*2^2 + 0*2^1 + 1*2^0
//
//	8 2*4+0
//	4 2*2+0
//	2 2*1+0
//	1 2*0+1
//	=> 1*2^3 + 0*2^2 + 0*2^1 + 0*2^0
//
//	13 (-2)*(-6)+1
//	-6 (-2)*3+0
//	3 (-2)*(-1)+1
//	-1 (-2)*1+1
//	1 (-2)*0 +1
//
//	=> 1*(-2)^4 + 1*(-2)^3 + 1*(-2)^2 + 0*(-2)^1 + 1*(-2)^0 = 16 - 8 + 4 + 1
//
//	-13 (-2)*7 + 1
//	7 (-2)*(-3) + 1
//	-3 (-2)*2 + 1
//	2 (-2)*(-1) + 0
//	-1 (-2)*1+1
//	1 (-2)*0 +1
//
//	=> 1*(-2)^5 + 1*(-2)^4 + 0*(-2)^3 + 1*(-2)^2 + 1*(-2)^1 + 1*(-2)^0 = - 32 + 16 + 4 - 2 +1

}
