import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Solution {
	
	static int N, M, K, targetA, targetB;
	static int[] aTime, bTime;
	
	static PriorityQueue<A> aWait;
	static PriorityQueue<B> bWait;
	
	static A[] aList;
	static B[] bList;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int TC = Integer.parseInt(br.readLine());
		
		for (int tc=1; tc<=TC; tc++) {
			
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			K = Integer.parseInt(st.nextToken());
			targetA = Integer.parseInt(st.nextToken());
			targetB = Integer.parseInt(st.nextToken());
			
			aTime = new int[N+1];	// 접수창구 소요시간
			bTime = new int[M+1];	// 정비창구 소요시간
			
			st = new StringTokenizer(br.readLine());
			for (int i=1; i<=N; i++) {
				aTime[i] = Integer.parseInt(st.nextToken());			
			}
			
			st = new StringTokenizer(br.readLine());
			for (int i=1; i<=M; i++) {
				bTime[i] = Integer.parseInt(st.nextToken());
			}	
			
			aWait = new PriorityQueue<>();	// 접수창구 대기
			bWait = new PriorityQueue<>();	// 정비창구 대기
			aList = new A[N+1];				// 현재 접수창구 진행중인 사람
			bList = new B[M+1];				// 현재 정비창구 진행중인 사람
			
			st = new StringTokenizer(br.readLine());
			for (int i=1; i<=K; i++) {
				aWait.add(new A(i, Integer.parseInt(st.nextToken()))); // new A(고객번호, 접수창구 도착시간)
			}

			int t = -1;		// 현재 시간
			int done = 0;	// 진행 완료 인원
			int sol = 0;	// 접수창구 번호와 정비창구 번호가 일치하는 고객들의 고객번호 합
			
			while(done < K) {
//				System.out.println(t);
//				System.out.println("aWait " + aWait);
//				System.out.println("aList " + Arrays.toString(aList));
//				System.out.println("bWait " + bWait);
//				System.out.println("bList " + Arrays.toString(bList));
//				System.out.println(); 
				
				t++;
				
				// 1. 정비중 고객 있다면 정비완료여부 확인
				for (int bId=1; bId<=M; bId++) {
					if (bList[bId] == null || t-bList[bId].sTime < bTime[bId]) continue; // 정비창구가 놀고 있거나 아직 완료되지 않았다면 패스
//					System.out.println(bList[bId].aId + " " + bList[bId].bId);
					if (bList[bId].aId == targetA && bList[bId].bId == targetB) { // 접수창구 번호와 정비창구 번호가 일치하는 고객이면 sol에 더해줌
						sol+=bList[bId].pId;
					}
					bList[bId] = null;
					done++;					
				}
				// 2. 정비창구를 이용하기 위해 대기중인 사람이 있고, 비는 정비창구가 있다면 정비 시작
				while (!bWait.isEmpty() && bWait.peek().dTime <= t) {
					int bId = 1;
					for (; bId<=M; bId++) {
						if (bList[bId] == null) break; 	// 비는 정비창구 확인
					}
					if (bId == M+1) break;				// 비는 정비창구가 없다면 패스
					bList[bId] = bWait.poll();			// 정비창구가 있다면 정비 시작
					bList[bId].setB(bId, t);			// 정비창구 번호와 정비시작시간도 같이 넘김
				}
				
				// 3. 접수중 고객 있다면 접수완료여부 확인 후 정비청구 대기에 추가
				for (int aId=1; aId<=N; aId++) {
					if (aList[aId] == null || t-aList[aId].sTime < aTime[aId]) continue; // 접수창구가 놀고 있거나 아직 완료되지 않았다면 패스
					bWait.add(new B(aList[aId].pId, aId, t)); // 접수 완료된 고객이 있다면 정비창구 대기에 추가 (이때 고객번호, 접수창구 번호도 같이 넘김)
					aList[aId] = null;
				}
				
				// 4. 접수창구를 이용하기 위해 대기중인 사람이 있고, 비는 접수창구가 있다면 접수 시작
				while (!aWait.isEmpty() && aWait.peek().dTime <= t) {
					int aId = 1;
					for (; aId<=N; aId++) {
						if (aList[aId] == null) break;	// 비는 접수창구 확인
					}
					if (aId == N+1) break;				// 비는 접수창구가 없다면 패스
					aList[aId] = aWait.poll();			// 접수창구가 있다면 접수 시작
					aList[aId].setA(aId, t);			// 접수창구 번호와 접수시작시간도 같이 넘김
				}
			
				
			}
			
			// 출력
			sb.append("#").append(tc).append(" ");
			if (sol == 0) {
				sb.append(-1);
			} else {
				sb.append(sol);
			}
			sb.append("\n");			
			
		}
		
		System.out.println(sb.toString());
		

	}

}

class A implements Comparable<A> {
	
	int pId, dTime, aId, sTime; // 고객번호, 접수창구 도착시간, 접구창구 번호, 접수 시작시간
	
	public A(int pId, int dTime) {
		this.pId = pId;
		this.dTime = dTime;
	}

	@Override
	public int compareTo(A o) {
		
		if (dTime != o.dTime) {
			return dTime-o.dTime;
		}
		return pId-o.pId;
	}
	
	public void setA(int aId, int sTime) { // 접수 시작되었다면 창구번호, 시작시간 기록
		this.aId = aId;
		this.sTime = sTime;
	}

	@Override
	public String toString() {
		return "A [pId=" + pId + ", dTime=" + dTime + ", aId=" + aId + ", sTime=" + sTime + "]";
	}
	
	

}

class B implements Comparable<B> {
	
	int pId, aId, dTime, bId, sTime; // 고객번호, 접수창구 번호, 정비창구 도착시간, 정비창구 번호, 정비 시작시간
	
	public B(int pId, int aId, int dTime) {
		this.pId = pId;
		this.aId = aId;
		this.dTime = dTime;
	}

	@Override
	public int compareTo(B o) {
		
		if (dTime != o.dTime) {
			return dTime-o.dTime;
		}
		return aId-o.aId;
	}
	
	public void setB(int bId, int sTime) { // 정비 시작되었다면 창구번호, 시작시간 기록
		this.bId = bId;
		this.sTime = sTime;
	}

	@Override
	public String toString() {
		return "B [pId=" + pId + ", aId=" + aId + ", dTime=" + dTime + ", bId=" + bId + ", sTime=" + sTime + "]";
	}
	
	
	
}
