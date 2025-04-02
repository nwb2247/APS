import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		int[] count = new int[N+1];		
		
		for (int i=1; i<=N; i++) {
			int n = i;
			while (n%2 == 0) {
				n/=2;
				count[i]++;
			}
			while (n%3 == 0) {
				n/=3;
				count[i]++;
			}
			
			// 2로 나누거나 3으로 나는 과정만으로는 1를 만들 수 없는 경우는 0으로 리셋
			if (n != 1) {
				count[i] = 0;		
			}
		}
		
		// 1씩 증가하면서 차례로 해당 i에 대한 최솟값을 구해나감
		for (int i=2; i<=N; i++) { // 1은 원래 0인것이 맞으므로 패스
			if (count[i] != 0) continue; // 0이 아닌 경우, 이미 값이 구해진 경우는 그것이 최솟값이므로 냅둠.
			
			// 해결 경우가 아니라면 (즉 0이면) 이미 해결된 경우에 접근 가능할 때까지 1씩 빼줌 (3이나 2로 나누는 경우가 되도록)
			int r3 = i%3;
			int r2 = i%2;
			
			int div3;
			int div2;
			
			// div3 결정
			if (r3 != 0) {
				div3 = count[i - r3] + r3; // 나머지가 1, 2인경우 3의 배수가 되도록하여 빼줌
			} else {
				div3 = count[i/3] + 1; // 나머지가 0인경우
			}
					
			if (r2 != 0) {
				div2 = count[i - r2] + r2;
			} else {
				div2 = count[i/2] + 1;
			}
			
			count[i] = Math.min(div3, div2);
			
		}
		
//		for (int i=1; i<=N; i++) {
//			System.out.println(i + " " + count[i]);
//		}
		
		System.out.println(count[N]);

	}

}
