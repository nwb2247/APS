import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		char[] chars = br.readLine().toCharArray();
		
		// 스택으로도 풀 수 있음
		
		int count = 0; // 지금까지 조각
		int cur = 0; // 현재 자를 대상인 막대기 수
		for (int i=0; i<chars.length; i++) {
			if (chars[i] == '(') {
				if (chars[i+1] == ')') { // 레이저라면, cur만큼 더해줌
					count += cur;
				} else {
					cur++;				// 자를 대상 막대가 하나 더 추가됨
				}
			} else { // ')'
				if (chars[i-1] == '(') {	// 레이저, 전 iter에서 더해줬으므로 패스
					continue;
				} else {					// 자를 대상 막대가 하나 감소하고, 조각이 하나 추가됨
					cur--;
					count++;
				}
			}
		}
		
		System.out.println(count);
	}

}
