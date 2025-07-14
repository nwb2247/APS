import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(br.readLine()); // 홀수
		int[] cnt = new int[8001];
		
		// 평균
		for (int i=0; i<N; i++) {
			cnt[Integer.parseInt(br.readLine())+4000]++;
		}
		
		int sum = 0;
		for (int i=0; i<8001; i++) {
			sum += cnt[i]*(i-4000);
		}
		int mean = Math.round(((float) sum)/N);
		
		// 최빈값
		int[] freqNum = new int[2];
		freqNum[1] = -1;
		for (int i=1; i<8001; i++) {
			if (cnt[i] > cnt[freqNum[0]]) {
				freqNum[0] = i;
				freqNum[1] = -1;
			} else if (cnt[i] == cnt[freqNum[0]] && freqNum[1] == -1){
				freqNum[1] = i;
			}
		}
		int freq = freqNum[1]==-1?freqNum[0]:freqNum[1];
		freq -= 4000;
		
		// 범위
		int min = 0;
		int max = 0;
		for (int i=0; i<8001; i++) {
			if (cnt[i] != 0) {
				min = i-4000;
				break;
			}
		}
		for (int i=8000; i>=0; i--) {
			if (cnt[i] != 0) {
				max = i-4000;
				break;
			}
		}
		int range = max-min;
		
		// 중앙값
		int c = N/2+1;
		int median = 0;
		for (int i=0; i<8001; i++) {
			if (c > cnt[i]) {
				c -= cnt[i];
				cnt[i] = 0;
			} else {
				median = i-4000;
				break;
			}
		}
		
		sb.append(mean).append("\n");
		sb.append(median).append("\n");
		sb.append(freq).append("\n");
		sb.append(range);
		System.out.println(sb.toString());
		
	}
    
}